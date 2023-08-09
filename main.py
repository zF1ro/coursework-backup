import requests
import os
import json
import datetime
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
    #Скачиваем информацию о фотографиях профиля
    with open('images_vk.json', 'w') as f:
        json.dump(main.get_photos(), f)
        print('Done with downloading photos information from vk') 
    
    vk_photos_info_json = main.get_photos()

    vk_photos_info = {}

    for id_numb, photo in enumerate(vk_photos_info_json['response']['items']):
        vk_photos_info[id_numb] = id_numb


    pprint(vk_photos_info)
