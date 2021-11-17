import requests
from .models import TeleSetting

token = '2132138421:AAHHAY1qUBdB-f8nf4hABTbOwZ9EcAXuY3s'
chat_id = '-614536253'
text = 'TEst2'


def sendTelegram(tg_name, tg_phone):
    if TeleSetting.objects.get(pk=1):
        settings = TeleSetting.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            a = text.find('{')
            b = text.find('}')
            c = text.rfind('{')
            d = text.rfind('}')

            part_1 = text[0:a]
            part_2 = text[b + 1:c]
            part_3 = text[d:-1]

            text_slize = part_1 + tg_name + part_2 + tg_phone + part_3

        else:
            text_slize = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slize
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Все ОК сообщение отправленно!')
    else:
        pass
