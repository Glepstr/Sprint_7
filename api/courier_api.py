import requests
import allure
from data import BASE_URL, COURIER_ENDPOINT, COURIER_LOGIN_ENDPOINT

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