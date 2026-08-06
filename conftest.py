import pytest
import allure
import requests
from helpers import register_new_courier_and_return_login_password, delete_courier, get_courier_id
from data import BASE_URL, ORDER_ENDPOINT, COURIER_ENDPOINT

@pytest.fixture(scope='function')
def create_courier():
    """Фикстура для создания курьера"""
    login, password, first_name = register_new_courier_and_return_login_password()
    yield login, password, first_name
    # Удаляем курьера после теста
    if login and password:
        courier_id = get_courier_id(login, password)
        if courier_id:
            delete_courier(courier_id)

@pytest.fixture(scope='function')
def create_order():
    """Фикстура для создания заказа"""
    order_data = {
        "firstName": "Test",
        "lastName": "User",
        "address": "Test Address 123",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2024-12-31",
        "comment": "Test comment"
    }
    
    response = requests.post(f'{BASE_URL}{ORDER_ENDPOINT}', json=order_data)
    track = response.json().get('track')
    order_id = None
    
    if track:
        # Получаем id заказа по треку
        track_url = f'{BASE_URL}/api/v1/orders/track?t={track}'
        order_response = requests.get(track_url)
        if order_response.status_code == 200:
            order_id = order_response.json().get('order', {}).get('id')
    
    yield track, order_id, order_data