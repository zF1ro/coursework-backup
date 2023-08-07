import requests
import os
import json
from pprint import pprint


with open('git-ignore/token.txt', 'r') as f:
    TOKEN = f.read()
APP_ID = 51721514
USER_ID = 640426005


class VkDownloader:

    def __init__(self, token):
        self.token = token

    def get_photos(self):

        url = 'https://api.vk.com/method/photos.get'
        params = {
                    'owner_id': USER_ID,
                    'album_id': 'profile',
                    'access_token': self.token,
                    'v': 5.131,
                    'extended': 1,
                    'photo_sizes': '1',
                    'rev' : 0,
                    'offset' : 0
                  }
        res = requests.get(url=url, params=params)
        return res.json()
    

if __name__ == '__main__':
    main = VkDownloader(TOKEN)
    with open('images_vk.json', 'w') as f:
        json.dump(main.get_photos(), f)