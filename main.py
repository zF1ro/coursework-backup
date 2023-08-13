import requests
import os
import json
import datetime
from pprint import pprint


with open('git-ignore/token.txt', 'r') as f:
    TOKEN = f.read()


class VkDownloader:

    def __init__(self, token, vk_id):
        self.token = token
        self.vk_id = vk_id

    def get_avatars(self):

        url = 'https://api.vk.com/method/photos.get'
        params = {
                    'owner_id': self.vk_id,
                    'album_id': 'profile',
                    'access_token': self.token,
                    'v': 5.131,
                    'extended': 1,
                    'photo_sizes': '1',
                    'rev' : 0,
                    'offset' : 0
                  }
        res = requests.get(url=url, params=params)

        all_avatars_count = res.json()['response']['count']
        avatars = [] # Список всех загруженных фото
        max_size_avatar = {}
        temp = 0

        #Создаем папку для хранения аватарок
        if not os.path.exists('_vk_avatars'):
            os.mkdir('_vk_avatars')

        for avatar in res.json()['response']['items']:
            max_size = 0
            avatars_info = {}
            for size in avatar['sizes']:
                if size['height'] >= max_size:
                    max_size = size['height']
            if avatar['likes']['count'] not in max_size_avatar.keys():
                max_size_avatar[avatar['likes']['count']] = size['url']
                avatars_info['file_name'] = f"{avatar['likes']['count']}.jpg"
            else:
                max_size_avatar[f"{avatar['likes']['count']}" +
                                f" {datetime.datetime.fromtimestamp(avatar['date']).strftime('%Y-%m-%d %H-%M-%S')}"] = size['url']
                avatars_info['file_name'] = f"{avatar['likes']['count']}_{avatar['date']}.jpg"
            
            #Список для avatars.json
            avatars_info['size'] = size['type']
            avatars.append(avatars_info)
        #Скачиваем аватарки
        for avatar_name, avatar_url in max_size_avatar.items():
            with open(f'_vk_avatars/{avatar_name}.jpg', 'wb') as f:
                img = requests.get(avatar_url)
                f.write(img.content)

        print(f'Всего аватарок загружено: {all_avatars_count}')

        #Записываем в файл avatars.json
        with open('avatars.json', 'w') as f:
            json.dump(avatars, f, indent = 4)

class YandexUploader:
    def __init__(self, token:str):
        self.token = token
    
    def folder_create(self):
        url = f"https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {ya_token}"
        }
        params = {
            "path": f"{'_vk_avatars'}",
            "overwrite": "false"
        }
        response = requests.put(url=url, headers=headers, params=params)

    def upload(self, file_path: str):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {ya_token}"
        }
        params = {
            "path": f"{'_vk_avatars'}/{file_name}",
            "overwrite": "true"}
        # Получение ссылки на загрузку
        response = requests.get(url=url, headers=headers, params=params)
        href = response.json().get('href')

        # Загрузка файла
        uploader = requests.put(href, data=open(files_path, 'rb'))

#Старт программы
if __name__ == '__main__':
    vk_id = input('Введите id пользователя VK: ')

    downloader = VkDownloader(TOKEN, vk_id)
    downloader.get_avatars()

    ya_token = input('Введите ваш токен для ЯндексДиска: ')
    uploader = YandexUploader(ya_token)
    uploader.folder_create()
    count = 0
    avatar_list = os.listdir('_vk_avatars')
    for avatar in avatar_list:
        file_name = avatar
        files_path = os.getcwd() + '\_vk_avatars\\' + avatar
        result = uploader.upload(files_path)
        count += 1
        print(f'Фотографий загружено на Яндекс диск: {count}')
    print('Резевное копирование аватарок завершено. Выходные данные сохранены в файл avatars.json')