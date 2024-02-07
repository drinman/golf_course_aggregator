from flask import Flask, render_template, request, jsonify
import requests
import os  # Import the os module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    location = request.form['location']
    courses = get_golf_courses(location)
    return render_template('results.html', courses=courses, google_maps_api_key=os.environ.get('GOOGLE_MAPS_API_KEY'))

def get_golf_courses(location):
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        "Authorization": "Bearer " + os.environ.get('YELP_API_KEY')  # Use environment variable for Yelp API key
    }
    params = {
        "term": "golf course",
        "location": location
    }
    response = requests.get(url, headers=headers, params=params)
    if response.ok:
        data = response.json()
        return data['businesses']
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True)
