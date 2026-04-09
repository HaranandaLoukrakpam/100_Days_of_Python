#request module in python

import requests

# Base URL for testing (public fake API)
BASE_URL = "https://jsonplaceholder.typicode.com"

# -----------------------------
# 1. GET REQUEST (Fetch data)
# -----------------------------
# Used to retrieve data from a server
response = requests.get(f"{BASE_URL}/posts/1")

print("GET Status Code:", response.status_code)   # HTTP status (200 = success)
print("GET Response JSON:", response.json())      # Convert JSON response to Python dict


# -----------------------------
# 2. POST REQUEST (Create data)
# -----------------------------
# Used to send data to the server and create a resource
data = {
    "title": "Test Post",
    "body": "This is a test",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=data)

print("\nPOST Status Code:", response.status_code)
print("POST Response:", response.json())


# -----------------------------
# 3. PUT REQUEST (Update entire resource)
# -----------------------------
# Used to completely replace an existing resource
updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
}

response = requests.put(f"{BASE_URL}/posts/1", json=updated_data)

print("\nPUT Status Code:", response.status_code)
print("PUT Response:", response.json())


# -----------------------------
# 4. PATCH REQUEST (Partial update)
# -----------------------------
# Used to update only specific fields of a resource
partial_update = {
    "title": "Partially Updated Title"
}

response = requests.patch(f"{BASE_URL}/posts/1", json=partial_update)

print("\nPATCH Status Code:", response.status_code)
print("PATCH Response:", response.json())


# -----------------------------
# 5. DELETE REQUEST (Remove resource)
# -----------------------------
# Used to delete a resource from the server
response = requests.delete(f"{BASE_URL}/posts/1")

print("\nDELETE Status Code:", response.status_code)
print("DELETE Response (usually empty):", response.text)


# -----------------------------
# 6. HEAD REQUEST (Headers only)
# -----------------------------
# Fetches only headers, not the body (useful for metadata)
response = requests.head(f"{BASE_URL}/posts")

print("\nHEAD Status Code:", response.status_code)
print("HEAD Headers:", response.headers)


# -----------------------------
# 7. CUSTOM HEADERS
# -----------------------------
# Used to send additional information (e.g., API keys, user-agent)
headers = {
    "User-Agent": "MyPythonApp/1.0"
}

response = requests.get(f"{BASE_URL}/posts", headers=headers)

print("\nCustom Headers Request Status:", response.status_code)


# -----------------------------
# 8. QUERY PARAMETERS
# -----------------------------
# Used to filter/search data via URL parameters
params = {
    "userId": 1
}

response = requests.get(f"{BASE_URL}/posts", params=params)

print("\nQuery Params Response:", response.json())


# -----------------------------
# 9. TIMEOUT (Prevent hanging)
# -----------------------------
# Stops request if server takes too long
try:
    response = requests.get(f"{BASE_URL}/posts", timeout=2)
    print("\nTimeout Request Successful")
except requests.exceptions.Timeout:
    print("\nRequest timed out!")


# -----------------------------
# 10. ERROR HANDLING
# -----------------------------
# Raises exception for bad status codes (4xx, 5xx)
try:
    response = requests.get(f"{BASE_URL}/invalid_endpoint")
    response.raise_for_status()  # Raises HTTPError if failed
except requests.exceptions.HTTPError as e:
    print("\nHTTP Error occurred:", e)


# -----------------------------
# 11. SESSION (Persistent connection)
# -----------------------------
# Keeps connection alive, stores cookies, improves performance
with requests.Session() as session:
    session.headers.update({"User-Agent": "SessionExample"})
    
    response = session.get(f"{BASE_URL}/posts/1")
    print("\nSession GET Response:", response.json())


# -----------------------------
# 12. DOWNLOADING FILES
# -----------------------------
# Used to download files (images, PDFs, etc.)
file_url = "https://via.placeholder.com/150"

response = requests.get(file_url)

with open("downloaded_image.png", "wb") as file:
    file.write(response.content)  # Write binary content

print("\nFile downloaded successfully!")
