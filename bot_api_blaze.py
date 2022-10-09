import requests
import telegram 
import time


TOKEN = 'seu token'

bot = telegram.Bot(TOKEN)

chat_id = 'seu id'

while True:

    url = 'https://blaze.com/api/roulette_games/recent'

    response = requests.get(url)

    r = response.json()

    ray = []

    for x in range(len(r)):
        val = r[x]['color']
        if val == 1:
            val = 'Vermelho'

        if val == 2:
            val = 'Preto'

        if val == 0:
            val = 'Branco'

        ray.append(val)

    print(ray)

    def resultado(num):
        if num[0:4] == ['Preto', 'Vermelho', 'Vermelho', 'Vermelho']:

            msg = '''✅ GREEN no ⚫'''
            mensagem = bot.send_message(chat_id=chat_id, text=msg)
            time.sleep(40)
            mensagem.delete()
            

        elif num[0:4] == ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:

            text = '''✅ LOSS'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(5)

        elif num[0:3] == ['Vermelho', 'Vermelho', 'Vermelho']:

            text = '''✅ Entrada confirmada, entrar no ⚫
                      Buscar apoio no ⚪'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(5)

        elif num[0:2] == ['Vermelho', 'Vermelho']:

            text = '''✅ Possivel entrada no ⚫
                Buscar apoio no ⚪'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(5)

        elif num[0:4] == ['Vermelho', 'Preto', 'Preto', 'Preto']:

            text = '''✅ GREEN no 🔴'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(5)

        elif num[0:4] == ['Preto', 'Preto', 'Preto', 'Preto']:

            text = '''✅ LOSS'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(5)

        elif num[0:3] == ['Preto', 'Preto', 'Preto']:

            text = '''✅ Entrada confirmada, entrar no 🔴
                   Buscar apoio no ⚪'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(5)

        elif num[0:2] == ['Preto', 'Preto']:

            text = '''✅ Possivel entrada no 🔴
                 Buscar apoio no ⚪ '''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(5)

    resultado(ray)

    time.sleep(5)
