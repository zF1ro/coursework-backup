import requests
import json
from urllib.parse import urlencode

APP_ID = 51721514
OAUTH_BASE_URL = "https://oauth.vk.com/authorize"

params = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'photos',
    'response_type': 'token',
    'v' : 5.131
}

oauth_url = f'{OAUTH_BASE_URL}?{urlencode(params)}'

print(oauth_url)