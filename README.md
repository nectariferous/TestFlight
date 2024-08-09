# TestFlight Store 📱🚀

[![Fetch and Process URLs](https://github.com/nectariferous/TestFlight/actions/workflows/fetch_urls.yml/badge.svg)](https://github.com/nectariferous/TestFlight/actions/workflows/fetch_urls.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10.12+](https://img.shields.io/badge/python-3.10.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)

TestFlight Store is a Flask-based web application designed to manage and display information about apps available on TestFlight. The application fetches app data from GitHub, processes it, and provides various endpoints to interact with the data.

🌐 **Live Demo**: [https://testflightstore-000431dbdbd9.herokuapp.com/](https://testflightstore-000431dbdbd9.herokuapp.com/)

## 🚀 Features

- **📋 App Listing**: Displays a list of apps with pagination
- **🔍 Search Functionality**: Allows users to search for apps by name
- **🏆 Top Apps**: Displays the top 5 apps
- **🎮 Top Games**: Displays the top 5 games
- **🌐 CORS Support**: Enables Cross-Origin Resource Sharing (CORS) for all routes
- **🖥️ Advanced View**: Provides a more detailed view of app information

## 📋 Prerequisites

| Requirement | Version |
|-------------|---------|
| Python      | 3.10.12 or higher |
| Flask       | Latest |
| Flask-CORS  | Latest |
| Requests    | Latest |
| BeautifulSoup4 | Latest |
| Coloredlogs | Latest |

## 🛠️ Installation

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

## 🚀 Deployment on Heroku

1. **Install the Heroku CLI**: Follow the instructions on the [Heroku CLI installation page](https://devcenter.heroku.com/articles/heroku-cli).

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

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For more information, please contact [nectariferous](mailto:owner@likhon.xyz).

## 💖 Support the Project

If you find this project helpful, consider supporting its development:

ETH Address: `0x00fC876d03172279E04CC30E5edCE103c3d23C1A`

Your support helps maintain and improve TestFlight Store!

## 🔬 Advanced View

The advanced view provides more detailed information about each app, including:

- App icon
- Version number
- Last update date
- Developer information
- Detailed description
- Screenshots (if available)

To access the advanced view, click on an app's name in the main listing.
