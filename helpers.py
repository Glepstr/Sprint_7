import requests
import random
import string
from data import BASE_URL, COURIER_ENDPOINT, COURIER_LOGIN_ENDPOINT, COURIER_DELETE_ENDPOINT

def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def register_new_courier_and_return_login_password():
    """Регистрирует нового курьера и возвращает его данные"""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(f'{BASE_URL}{COURIER_ENDPOINT}', data=payload)
    
    if response.status_code == 201:
        return login, password, first_name
    return None, None, None

def delete_courier(courier_id):
    """Удаляет курьера по id"""
    url = f'{BASE_URL}{COURIER_DELETE_ENDPOINT.format(courier_id)}'
    response = requests.delete(url)
    return response

def get_courier_id(login, password):
    """Получает id курьера по логину и паролю"""
    url = f'{BASE_URL}{COURIER_LOGIN_ENDPOINT}'
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get('id')
    return None