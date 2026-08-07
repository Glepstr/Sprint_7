import pytest
import allure
from helpers import generate_random_string
from api.courier_api import CourierAPI
from data import ERROR_MESSAGES

@allure.feature('Курьер')
@allure.story('Логин курьера')
class TestCourierLogin:
    
    @allure.title('Курьер может авторизоваться')
    def test_courier_login_success(self, create_courier):
        login, password, _ = create_courier
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = CourierAPI.login_courier(payload)
        assert response.status_code == 200
        assert 'id' in response.json()
    
    @allure.title('Для авторизации нужно передать все обязательные поля')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_courier_login_missing_field(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        payload.pop(missing_field)
        
        response = CourierAPI.login_courier(payload)
        assert response.status_code == 400
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_LOGIN_MISSING_FIELD']
    
    @allure.title('Система вернёт ошибку при неправильном логине или пароле')
    def test_courier_login_invalid_credentials(self, create_courier):
        login, _, _ = create_courier
        
        payload = {
            "login": login,
            "password": "wrongpassword"
        }
        
        response = CourierAPI.login_courier(payload)
        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_LOGIN_INVALID']
    
    @allure.title('Ошибка при авторизации под несуществующим пользователем')
    def test_courier_login_nonexistent(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        
        response = CourierAPI.login_courier(payload)
        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_LOGIN_INVALID']