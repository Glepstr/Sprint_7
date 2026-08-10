import requests
import allure
from data import BASE_URL, COURIER_ENDPOINT, COURIER_LOGIN_ENDPOINT, COURIER_DELETE_ENDPOINT

class CourierAPI:
    
    @staticmethod
    def create_courier(payload):
        """Создание курьера"""
        with allure.step(f"Создание курьера с данными: {payload}"):
            response = requests.post(f'{BASE_URL}{COURIER_ENDPOINT}', data=payload)
            return response
    
    @staticmethod
    def login_courier(payload):
        """Логин курьера"""
        with allure.step(f"Логин курьера с данными: {payload}"):
            response = requests.post(f'{BASE_URL}{COURIER_LOGIN_ENDPOINT}', data=payload)
            return response

    @staticmethod
    def delete_courier(courier_id):
        """Удаление курьера"""
        with allure.step(f"Удаление курьера с id: {courier_id}"):
            response = requests.delete(f'{BASE_URL}{COURIER_DELETE_ENDPOINT.format(courier_id)}')
            return response
    
    @staticmethod
    def get_courier_id(login, password):
        """Получение id курьера по логину и паролю"""
        with allure.step(f"Получение id курьера"):
            payload = {"login": login, "password": password}
            response = requests.post(f'{BASE_URL}{COURIER_LOGIN_ENDPOINT}', data=payload)
            if response.status_code == 200:
                return response.json().get('id')
            return None