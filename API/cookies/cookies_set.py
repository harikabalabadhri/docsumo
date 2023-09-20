import requests
# Define the URL for setting cookies
set_cookies_url = "https://httpbin.org/cookies/set?freeform="

# Set two key-value pairs as cookies
cookies_to_set = {"cookie1": "value1", "cookie2": "value2"}

# Make the GET request to set cookies
response = requests.get(set_cookies_url, cookies=cookies_to_set)

# Check if the response status code is 200 OK
if response.status_code == 200:
    # Make a GET request to retrieve cookies
    cookies_url = "https://httpbin.org/cookies"
    response = requests.get(cookies_url)

    # Verify if cookies are properly set
    if all(key in response.json()["cookies"] for key in cookies_to_set.keys()):
        print("Cookies are properly set.")
    else:
        print("Cookies are not set as expected.")
else:
    print("Failed to set cookies.")
