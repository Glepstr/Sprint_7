import requests
import random
import string
from data import BASE_URL, COURIER_ENDPOINT, COURIER_LOGIN_ENDPOINT, COURIER_DELETE_ENDPOINT

def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))