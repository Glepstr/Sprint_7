import pytest
import allure
import requests
from data import ERROR_MESSAGES, COURIER_ENDPOINT, BASE_URL
from helpers import generate_random_string, register_new_courier_and_return_login_password
from api.courier_api import CourierAPI

@allure.feature('Курьер')
@allure.story('Создание курьера')
class TestCourierCreate:
    
    @allure.title('Курьера можно создать')
    def test_create_courier_success(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        assert login is not None
        assert password is not None
        assert first_name is not None
    
    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, create_courier):
        login, password, first_name = create_courier
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = CourierAPI.create_courier(payload)
        assert response.status_code == 409
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_CREATE_EXIST']
    
    @allure.title('Нужно передать все обязательные поля для создания курьера')
    def test_create_courier_missing_login(self):
        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        response = CourierAPI.create_courier(payload)
        assert response.status_code == 400
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_CREATE_MISSING_FIELD']
    
    @allure.title('Успешный запрос возвращает правильный код ответа и тело')
    def test_create_courier_success_response(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = CourierAPI.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
    
    @allure.title('Возвращается ошибка при отсутствии обязательных полей (login или password)')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_required_fields(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        payload.pop(missing_field)
        
        response = CourierAPI.create_courier(payload)
        assert response.status_code == 400
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_CREATE_MISSING_FIELD']

    @allure.title('Можно создать курьера без поля firstName')
    def test_create_courier_without_firstname(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        
        response = CourierAPI.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}