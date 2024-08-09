from flask import Flask, render_template, jsonify, request
import json
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the app data
try:
    with open('output.json', 'r') as file:
        all_apps = json.load(file)
except IOError as e:
    print(f"Error reading file: {e}")
    all_apps = []
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    all_apps = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/apps')
def api_apps():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    start = (page - 1) * limit
    end = start + limit
    return jsonify(all_apps[start:end])

@app.route('/api/search', methods=['POST'])
def search():
    query = request.json.get('query', '').lower()
    filtered_apps = [app for app in all_apps if query in app['name'].lower()]
    return jsonify(filtered_apps)

@app.route('/api/top-apps')
def top_apps():
    # In a real scenario, you'd implement logic to determine top apps
    # For now, we'll just return the first 5 apps
    return jsonify(all_apps[:5])

@app.route('/api/top-games')
def top_games():
    # Similar to top_apps, but you'd filter for games
    games = [app for app in all_apps if 'game' in app.get('category', '').lower()]
    return jsonify(games[:5])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


