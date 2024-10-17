import requests
import time
from datetime import datetime

API_URL = "https://ml-recipe-api.onrender.com/api/display_recipe"

INTERVAL = 80

def send_request():
    try:
        response = requests.get(API_URL)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response.status_code == 200:
            print(f"{timestamp} - Received 200 OK response from {API_URL}")
        else:
            print(f"{timestamp} - Received non-200 response: {response.status_code}")
    except requests.RequestException as e:
        print(f"{timestamp} - Error sending request: {e}")

def main():
    print(f"Keep-Alive Bot started. Sending requests to {API_URL} every {INTERVAL} seconds.")
    print("Press Ctrl+C to stop the bot.")
    
    while True:
        send_request()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()