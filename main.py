import re
import requests
from bs4 import BeautifulSoup

def get_phone_numbers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    phone_numbers = re.findall(r'\+?[78]?\s?\(?\d{3}\)?\s?\d{3}[-\.\s]?\d{2}[-\.\s]?\d{2}', soup.text)

    phone_numbers = [re.sub(r'\D', '', phone) for phone in phone_numbers]
    phone_numbers = ['8' + phone[1:] if phone.startswith('7') else phone for phone in phone_numbers]
    phone_numbers = ['8495' + phone[1:] if len(phone) == 7 else phone for phone in phone_numbers]

    return phone_numbers

print(get_phone_numbers('https://repetitors.info'))
