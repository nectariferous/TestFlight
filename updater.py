import os
import time
import json
import logging
import requests
from bs4 import BeautifulSoup
import coloredlogs

# Configure logging with colored output
coloredlogs.install(level='DEBUG', fmt='%(asctime)s - %(levelname)s - %(message)s')

def fetch_app_info(app_url, retries=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
    }

    for attempt in range(retries):
        try:
            response = requests.get(app_url, headers=headers, timeout=10)
            response.raise_for_status()
            break
        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt + 1} failed for URL {app_url}: {e}")
            if attempt < retries - 1:
                time.sleep(2)  # Wait before retrying
            else:
                logging.error(f"Error fetching the URL {app_url}: {e}")
                return None, None

    soup = BeautifulSoup(response.content, 'html.parser')
    meta_tags = soup.find_all('meta')

    logo_url = None
    app_name = None

    for tag in meta_tags:
        if tag.get('property') == 'og:image:secure_url':
            logo_url = tag.get('content')
        elif tag.get('property') == 'og:title':
            app_name = tag.get('content').replace('Join the ', '').replace(' beta', '')

    if not logo_url:
        logging.warning(f"No logo found for {app_url}")
    if not app_name:
        logging.warning(f"No app name found for {app_url}")

    return app_name, logo_url

def load_existing_results(output_file):
    if os.path.exists(output_file):
        with open(output_file, 'r') as json_file:
            return json.load(json_file)
    return []

def save_results(results, output_file):
    existing_results = load_existing_results(output_file)
    unique_results = {result['name']: result for result in existing_results + results}
    unique_results_list = list(unique_results.values())

    try:
        with open(output_file, 'w') as json_file:
            json.dump(unique_results_list, json_file, indent=4)
        logging.info(f"Data has been written to {output_file}")
    except IOError as e:
        logging.error(f"Error writing to file {output_file}: {e}")

def search_github_for_urls(page=1):
    search_query = 'testflight.apple.com/join'
    url = f'https://api.github.com/search/code?q={search_query}&type=code&per_page=100&page={page}'
    headers = {
        'Authorization': f'token {os.getenv("TOKENS")}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        results = response.json().get('items', [])
        urls = []
        for item in results:
            if 'html_url' in item:
                urls.append(item['html_url'])
        return urls
    else:
        logging.error(f"Error searching GitHub: {response.status_code}")
        return []

def extract_testflight_links(github_urls):
    testflight_links = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
    }

    for url in github_urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.warning(f"Error fetching the URL {url}: {e}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)

        for link in links:
            if 'testflight.apple.com/join' in link['href']:
                testflight_links.append(link['href'])

    return testflight_links

def main():
    output_file = 'output.json'  # Change this to your desired output file path

    page = 1
    while True:
        github_urls = search_github_for_urls(page)
        if not github_urls:
            break

        testflight_links = extract_testflight_links(github_urls)
        existing_results = load_existing_results(output_file)
        existing_names = {result['name'] for result in existing_results}
        results = []

        for link in testflight_links:
            app_name, logo_url = fetch_app_info(link)
            if app_name and app_name not in existing_names and logo_url and logo_url != "https://testflight.apple.com/images/testflight-1200_27.jpg":
                results.append({
                    'name': app_name,
                    'url': link,
                    'logo': logo_url
                })
            else:
                logging.warning(f"Skipping URL {link} due to invalid app name or logo.")

            # Save results instantly for development check
            save_results(results, output_file)

        logging.info(f"Total apps saved: {len(results)}")
        page += 1

if __name__ == "__main__":
    main()
