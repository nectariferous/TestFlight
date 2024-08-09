import requests
from bs4 import BeautifulSoup
import logging
import json
import time
import coloredlogs
import os

# Configure logging with colored output
coloredlogs.install(level='DEBUG', fmt='%(asctime)s - %(levelname)s - %(message)s')

def fetch_app_logo(app_url, retries=3):
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
                return None

    soup = BeautifulSoup(response.content, 'html.parser')
    meta_tag = soup.find('meta', {'property': 'og:image:secure_url'})

    if meta_tag and 'content' in meta_tag.attrs:
        return meta_tag.attrs['content']
    else:
        logging.warning(f"No logo found for {app_url}")
        return None

def fetch_app_name(app_url, retries=3):
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
                return None

    soup = BeautifulSoup(response.content, 'html.parser')
    meta_tag = soup.find('meta', {'property': 'og:title'})

    if meta_tag and 'content' in meta_tag.attrs:
        return meta_tag.attrs['content'].replace('Join the ', '').replace(' beta', '')
    else:
        return None

def load_existing_results(output_file):
    if os.path.exists(output_file):
        with open(output_file, 'r') as json_file:
            return json.load(json_file)
    return []

def save_results(results, output_file):
    existing_results = load_existing_results(output_file)
    unique_results = {result['url']: result for result in existing_results + results}
    unique_results_list = list(unique_results.values())

    try:
        with open(output_file, 'w') as json_file:
            json.dump(unique_results_list, json_file, indent=4)
        logging.info(f"Data has been written to {output_file}")
    except IOError as e:
        logging.error(f"Error writing to file {output_file}: {e}")

def search_github_for_urls():
    search_query = 'testflight.apple.com/join'
    url = f'https://api.github.com/search/code?q={search_query}'
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

def main():
    output_file = 'output.json'  # Change this to your desired output file path

    urls = search_github_for_urls()
    existing_results = load_existing_results(output_file)
    existing_urls = {result['url'] for result in existing_results}
    results = []

    for url in urls:
        if url in existing_urls:
            logging.info(f"Skipping already processed URL: {url}")
            continue

        logo_url = fetch_app_logo(url)
        if logo_url:
            app_name = fetch_app_name(url)
            if app_name and app_name != "TestFlight - Apple" and logo_url != "https://testflight.apple.com/images/testflight-1200_27.jpg":
                results.append({
                    'name': app_name,
                    'url': url,
                    'logo': logo_url
                })
            else:
                logging.warning(f"Skipping URL {url} due to invalid app name or logo.")
        else:
            logging.warning(f"Skipping URL {url} due to missing logo.")

        # Save results instantly for development check
        save_results(results, output_file)

    logging.info(f"Total apps saved: {len(results)}")

if __name__ == "__main__":
    main()
