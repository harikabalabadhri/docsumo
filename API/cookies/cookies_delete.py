import requests

# Define the URL for deleting a cookie
delete_cookie_url = "https://httpbin.org/cookies/delete?freeform="

# Specify the name of the cookie to delete
cookie_to_delete = "cookie1"  # Change this to the name of the cookie you want to delete

# Make the GET request to delete the specified cookie
response = requests.get(delete_cookie_url, cookies={cookie_to_delete: ""})

# Check if the response status code is 200 OK
if response.status_code == 200:
    # Make a GET request to retrieve cookies
    cookies_url = "https://httpbin.org/cookies"
    response = requests.get(cookies_url)

    # Verify if the deleted cookie is no longer present
    if cookie_to_delete not in response.json()["cookies"]:
        print(f"The '{cookie_to_delete}' cookie has been deleted.")
    else:
        print(f"The '{cookie_to_delete}' cookie was not deleted.")
else:
    print("Failed to delete the cookie.")
