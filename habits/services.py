from config.settings import TG_BOT_KEY
import requests


def send_tg_message(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id
    }

    response = requests.get(f'https://api.telegram.org/bot{TG_BOT_KEY}/sendMessage', params=params)

    if response.status_code != 200:
        print(f"Failed: {response.text}")
    else:
        print(f"Successfully {chat_id}: {message}")


def is_today(periodicity, start_date, today):
    delta = (today - start_date).days

    if periodicity == '1_day':
        return True
    elif periodicity == '3_days':
        return delta % 3 == 0
    elif periodicity == '7_days':
        return delta % 7 == 0
    return False

