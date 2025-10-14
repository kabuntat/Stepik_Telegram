import requests
import time

KITTEN_API_URL = 'https://api.thecatapi.com/v1/images/search'

kitten_request = requests.get(KITTEN_API_URL).json()

print(kitten_request[0]["url"])