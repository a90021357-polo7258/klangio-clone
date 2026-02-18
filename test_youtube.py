import requests
import json

# API Endpoint
url = "http://localhost:8000/api/process-youtube"

# Test YouTube URL (Rick Roll - definitely available)
test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

payload = {
    "url": test_url,
    "instrument": "piano" # Default
}

try:
    print(f"Sending YouTube request to {url}...")
    response = requests.post(url, json=payload)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print("Success!")
        print(f"Title: {result['data']['title']}")
        print(f"Message: {result['data']['message']}")
    else:
        print(f"Error: {response.text}")

except Exception as e:
    print(f"Request failed: {e}")
