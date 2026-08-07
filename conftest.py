import pytest
import allure
import requests
from helpers import generate_random_string
from api.courier_api import CourierAPI
from api.order_api import OrderAPI
from data import BASE_URL, ORDER_ENDPOINT, ORDER_DATA

@pytest.fixture(scope='function')
def create_courier():
    """Фикстура создает курьера и удаляет его после теста"""
    # Генерация данных
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    # Создание курьера
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = CourierAPI.create_courier(payload)
    
    # Проверка создания
    if response.status_code == 201:
        yield login, password, first_name
    else:
        yield None, None, None
    
    # Удаление курьера после теста
    if login and password:
        courier_id = CourierAPI.get_courier_id(login, password)
        if courier_id:
            CourierAPI.delete_courier(courier_id)

@pytest.fixture(scope='function')
def create_order():
    """Фикстура создает заказ"""
    # Используем данные из data.py
    order_data = ORDER_DATA.copy()
    response = OrderAPI.create_order(order_data)
    
    if response.status_code == 201:
        track = response.json().get('track')
        # Получаем order_id по треку
        order_response = OrderAPI.get_order_by_track(track)
        order_id = None
        if order_response.status_code == 200:
            order_id = order_response.json().get('order', {}).get('id')
        yield track, order_id
    else:
        yield None, None

@pytest.fixture(scope='function')
def create_courier_and_order():
    """Фикстура создает курьера и заказ для тестов принятия заказа"""
    # Создаем курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    courier_payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    CourierAPI.create_courier(courier_payload)
    courier_id = CourierAPI.get_courier_id(login, password)
    
    # Создаем заказ
    order_data = ORDER_DATA.copy()
    order_response = OrderAPI.create_order(order_data)
    track = order_response.json().get('track')
    
    # Получаем order_id
    order_info = OrderAPI.get_order_by_track(track)
    order_id = order_info.json().get('order', {}).get('id')
    
    yield courier_id, order_id, login, password
    
    # Удаляем курьера после теста
    if courier_id:
        CourierAPI.delete_courier(courier_id)