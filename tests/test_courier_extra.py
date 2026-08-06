import pytest
import allure
from data import ERROR_MESSAGES, BASE_URL, COURIER_DELETE_ENDPOINT
from helpers import register_new_courier_and_return_login_password, delete_courier, get_courier_id
from api.courier_extra_api import CourierExtraAPI
from api.order_api import OrderAPI

@allure.feature('Дополнительные тесты')
class TestCourierExtra:
    
    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        courier_id = get_courier_id(login, password)
        
        response = CourierExtraAPI.delete_courier(courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}
    
    @allure.title('Ошибка при удалении без id')
    def test_delete_courier_without_id(self):
        url = f'{BASE_URL}{COURIER_DELETE_ENDPOINT.format("")}'
        response = CourierExtraAPI.delete_courier("")
        # В зависимости от реализации API, может вернуть 404 или 400
        assert response.status_code in [400, 404]
    
    @allure.title('Ошибка при удалении с несуществующим id')
    def test_delete_courier_invalid_id(self):
        response = CourierExtraAPI.delete_courier(999999)
        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_DELETE_NOT_FOUND']
    
    @allure.title('Успешное принятие заказа курьером')
    def test_accept_order_success(self):
        # 1. Создаем курьера
        login, password, first_name = register_new_courier_and_return_login_password()
        assert login is not None, "Не удалось создать курьера"
        
        courier_id = get_courier_id(login, password)
        assert courier_id is not None, "Не удалось получить ID курьера"
        
        # 2. Создаем заказ
        order_data = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test Address",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2024-12-31"
        }
        order_response = OrderAPI.create_order(order_data)
        assert order_response.status_code == 201, "Не удалось создать заказ"
        
        track = order_response.json().get('track')
        assert track is not None, "Не получен track заказа"
        
        # 3. Получаем order_id по track
        order_info_response = CourierExtraAPI.get_order_by_track(track)
        assert order_info_response.status_code == 200, "Не удалось получить информацию о заказе"
        
        order_id = order_info_response.json().get('order', {}).get('id')
        assert order_id is not None, "Не удалось получить ID заказа"
        
        # 4. Принимаем заказ (передаем order_id, а не track!)
        accept_response = CourierExtraAPI.accept_order(order_id, courier_id)
        assert accept_response.status_code == 200, f"Ожидался 200, получен {accept_response.status_code}"
        assert accept_response.json() == {"ok": True}
        
        # 5. Чистим данные
        delete_courier(courier_id)
    
    @allure.title('Ошибка при принятии заказа без id курьера')
    def test_accept_order_without_courier_id(self):
        response = CourierExtraAPI.accept_order(1, "")
        # В зависимости от реализации
        assert response.status_code in [400, 404]
    
    @allure.title('Ошибка при принятии заказа с неверным id курьера')
    def test_accept_order_invalid_courier(self):
        response = CourierExtraAPI.accept_order(1, 999999)
        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['ORDER_ACCEPT_INVALID_COURIER']
    
    @allure.title('Успешное получение заказа по номеру')
    def test_get_order_by_track_success(self):
        # Создаем заказ
        order_data = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test Address",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2024-12-31"
        }
        order_response = OrderAPI.create_order(order_data)
        track = order_response.json().get('track')
        
        response = CourierExtraAPI.get_order_by_track(track)
        assert response.status_code == 200
        assert 'order' in response.json()
    
    @allure.title('Ошибка при получении заказа без номера')
    def test_get_order_without_track(self):
        response = CourierExtraAPI.get_order_by_track("")
        assert response.status_code == 400
        assert response.json().get('message') == ERROR_MESSAGES['ORDER_TRACK_MISSING_NUMBER']
    
    @allure.title('Ошибка при получении заказа с несуществующим номером')
    def test_get_order_invalid_track(self):
        response = CourierExtraAPI.get_order_by_track(999999)
        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['ORDER_TRACK_NOT_FOUND']