import requests
import datetime

URL = "https://boom.com/"

def log_status(status):
    with open("app_health_log", "a"):
        f.write(f"{dt.dt.now()} - {status}\n")
    print(status)

try:
    response = request.get(URL, timeout=5)
    if response.status_code == 200:
        log_status(f"Application is UP and status code is {response.status_code}")
    else:
        log_status(f"Application is DOWN and status code is {response.status_code}")
except request.exceptions.RequestException as e:
    log_status(f"Application is DOWN. Error: {e}")
