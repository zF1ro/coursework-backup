import requests
import json
from urllib.parse import urlencode

# https://oauth.vk.com/authorize

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

#https://oauth.vk.com/blank.html#access_token=vk1.a.43BaJOTQfhTCcnxA9_Kf-zo7PfBHQ3L6MKIYMwKNAGfa868dIlZbDcZ0FXtkgp9jgQ0J_bkOcrNA8QyELGIPviuZ9tbyTd3BdlsOsiRywuDAF5FxzGfEsRmD6-ft-uI4EWu_sdxQVdCZrilcBgWqU9TqxE0CTmL0i4FJygrFC2hsocvsWUlOOb13mDPqsstr&expires_in=86400&user_id=640426005