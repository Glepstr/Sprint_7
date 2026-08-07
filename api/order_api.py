import requests
import allure
from data import BASE_URL, ORDER_ENDPOINT, ORDER_TRACK_ENDPOINT

class OrderAPI:
    
    @staticmethod
    def create_order(payload):
        """Создание заказа"""
        with allure.step(f"Создание заказа"):
            response = requests.post(f'{BASE_URL}{ORDER_ENDPOINT}', json=payload)
            return response
    
    @staticmethod
    def get_orders():
        """Получение списка заказов"""
        with allure.step("Получение списка заказов"):
            response = requests.get(f'{BASE_URL}{ORDER_ENDPOINT}')
            return response
    
    @staticmethod
    def get_order_by_track(track):
        """Получение заказа по треку"""
        with allure.step(f"Получение заказа по треку: {track}"):
            response = requests.get(f'{BASE_URL}{ORDER_TRACK_ENDPOINT}', params={'t': track})
            return response


    @staticmethod
    def accept_order(order_id, courier_id):
        """Принятие заказа курьером"""
        with allure.step(f"Принятие заказа {order_id} курьером {courier_id}"):
            url = f'{BASE_URL}{ORDER_ACCEPT_ENDPOINT.format(order_id)}'
            response = requests.put(url, params={'courierId': courier_id})
            return response