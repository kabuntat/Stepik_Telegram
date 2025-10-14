import requests
import time


API_URL = 'https://api.telegram.org/bot'
KITTEN_API_URL = 'https://api.thecatapi.com/v1/images/search'
DOG_API_URL = 'https://random.dog/woof.json'
FOX_API_URL = 'https://randomfox.ca/floof/'
BOT_TOKEN = '8118742897:AAFJFwUMg6DfM6zlOmYVokhefoYg0lKe4H0'
# TEXT = 'Ура! Классный апдейт!'
# MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while True:
    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            if any(x in result['message']['text'] for x in ['кот', 'кошка', 'cat', 'kitt', '🐈']):
                # print(result['message']['text'])
                kitten_request = requests.get(KITTEN_API_URL).json()
                kitten_photo_url = kitten_request[0]["url"]
                # print(kitten_photo_url)
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={kitten_photo_url}')
            elif any(x in result['message']['text'] for x in ['пес', 'собак', 'щенок', 'dog', '🐕']):
                # print(result['message']['text'])
                dog_request = requests.get(DOG_API_URL).json()
                # print(dog_request)
                dog_photo_url = dog_request["url"]
                # print(dog_photo_url)
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_photo_url}')
            elif any(x in result['message']['text'] for x in ['лис', 'fox', '🦊']):
                # print(result['message']['text'])
                fox_request = requests.get(FOX_API_URL).json()
                print(fox_request)
                fox_photo_url = fox_request["image"]
                # print(fox_photo_url)
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={fox_photo_url}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Only cats dogs and foxes are here')
    counter += 1