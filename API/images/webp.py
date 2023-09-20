import requests

# Define the URL and expected image extension
url = "https://httpbin.org/image/webp"
expected_extension = "image/webp"  # Change this to your expected extension

# Set the 'Accept' header
headers = {"Accept": expected_extension}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the response status code is 200 OK
if response.status_code == 200:
    # Extract the 'Content-Type' header
    content_type = response.headers.get("Content-Type")

    # Check if the actual image extension matches the expected extension
    if content_type == expected_extension:
        print("Image extension is as expected.")
    else:
        print("Image extension does not match the expected extension.")
else:
    print("Failed to retrieve the image.")