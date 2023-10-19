import requests
import webbrowser
import sys

# Your YouTube Data API v3 key
API_KEY_FILE = open("APIKEY.txt","r")
API_KEY = API_KEY_FILE.read()

# Base URL for the YouTube Data API v3 search endpoint
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

# Parameters for the search
params = {
    'part': 'snippet',
    'q': 'rain' if (len(sys.argv) <= 1) else str(sys.argv[1]),
    'type': 'video',
    'key': API_KEY,
    'maxResults': 1
}

# Make the API request
response = requests.get(SEARCH_URL, params=params)
response_data = response.json()

# Extract the video ID of the first result
video_id = response_data['items'][0]['id']['videoId']

# Open the video in the default web browser
webbrowser.open(f'https://www.youtube.com/watch?v={video_id}')

