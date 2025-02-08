import requests
import os
from huggingface_hub import login
# Replace with your read token
hf_token = os.getenv("HUGGINGFACE_TOKEN")
login(token=hf_token)

# Test the token by calling the Hugging Face API
response = requests.get(
    "https://huggingface.co/api/whoami-v2",
    headers={"Authorization": f"Bearer {hf_token}"}
)

if response.status_code == 200:
    print("Token is valid!")
    print("User Info:", response.json())
else:
    print("Token is invalid or there was an error.")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")