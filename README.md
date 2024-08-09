# TestFlight
Basic concept. An TestFlight app store is any digital storefront intended to allow search and review of software titles or other media offered for sale electronically.

TestFlightStore is a Flask-based web application designed to manage and display information about apps available on TestFlight. The application fetches app data from GitHub, processes it, and provides various endpoints to interact with the data.

## Features

- **App Listing**: Displays a list of apps with pagination.
- **Search Functionality**: Allows users to search for apps by name.
- **Top Apps**: Displays the top 5 apps.
- **Top Games**: Displays the top 5 games.
- **CORS Support**: Enables Cross-Origin Resource Sharing (CORS) for all routes.

## Prerequisites

- Python 3.10.12 or higher
- Flask
- Flask-CORS
- Requests
- BeautifulSoup4
- Coloredlogs

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/nectariferous/TestFlight.git
    cd TestFlight
    ```

2. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application**:

    ```sh
    python app.py
    ```

## Deployment on Heroku

1. **Install the Heroku CLI**:

    Follow the instructions on the [Heroku CLI installation page](https://devcenter.heroku.com/articles/heroku-cli).

2. **Log in to Heroku**:

    ```sh
    heroku login
    ```

3. **Create a new Heroku app**:

    ```sh
    heroku create your-app-name
    ```

4. **Push your code to Heroku**:

    ```sh
    git push heroku main
    ```

5. **Open your app in the browser**:

    ```sh
    heroku open
    ```

**
## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For more information, please contact [nectariferous](mailto:owner@likhon.xyz).
**
