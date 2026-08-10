import requests
import allure
from data import BASE_URL, COURIER_DELETE_ENDPOINT, ORDER_ACCEPT_ENDPOINT, ORDER_TRACK_ENDPOINT

class CourierExtraAPI:
    
    @staticmethod
    def delete_courier(courier_id):
        """Удаление курьера"""
        with allure.step(f"Удаление курьера с id: {courier_id}"):
            response = requests.delete(f'{BASE_URL}{COURIER_DELETE_ENDPOINT.format(courier_id)}')
            return response
    
    @staticmethod
    def accept_order(order_id, courier_id):
        """Принятие заказа курьером"""
        with allure.step(f"Принятие заказа {order_id} курьером {courier_id}"):
            url = f'{BASE_URL}{ORDER_ACCEPT_ENDPOINT.format(order_id)}'
            response = requests.put(url, params={'courierId': courier_id})
            return response
    
    @staticmethod
    def get_order_by_track(track):
        """Получение заказа по номеру трека"""
        with allure.step(f"Получение заказа по треку: {track}"):
            response = requests.get(f'{BASE_URL}{ORDER_TRACK_ENDPOINT}', params={'t': track})
            return response