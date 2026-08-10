# tests/test_order_accept.py
import pytest
import allure
from api.courier_api import CourierAPI
from api.order_api import OrderAPI
from helpers import generate_random_string
from data import ORDER_DATA

@allure.feature('Заказ')
@allure.story('Принятие заказа')
class TestOrderAccept:
    
    @allure.title('Успешное принятие заказа курьером')
    def test_accept_order_success(self, create_courier_and_order):
        courier_id, order_id, login, password = create_courier_and_order
        
        response = OrderAPI.accept_order(order_id, courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}
    
    @allure.title('Ошибка при принятии заказа с неверным id курьера')
    def test_accept_order_invalid_courier(self, create_order):
        track, order_id = create_order
        
        response = OrderAPI.accept_order(order_id, 999999)
        assert response.status_code == 404
        assert 'Курьера с таким id не существует' in response.json().get('message', '')
    
    @allure.title('Ошибка при принятии заказа с неверным id заказа')
    def test_accept_order_invalid_order(self, create_courier):
        login, password, _ = create_courier
        courier_id = CourierAPI.get_courier_id(login, password)
        
        response = OrderAPI.accept_order(999999, courier_id)
        assert response.status_code == 404
        assert 'Заказа с таким id не существует' in response.json().get('message', '')