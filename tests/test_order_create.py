import pytest
import allure
from data import COLORS
from api.order_api import OrderAPI
from helpers import generate_random_string

@allure.feature('Заказ')
@allure.story('Создание заказа')
class TestOrderCreate:
    
    @pytest.fixture(scope='function')
    def order_data(self):
        return {
            "firstName": generate_random_string(10),
            "lastName": generate_random_string(10),
            "address": "Test Address 123",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2024-12-31",
            "comment": "Test comment"
        }
    
    @allure.title('Можно указать только цвет BLACK')
    @pytest.mark.parametrize('color', [[COLORS['BLACK']], [COLORS['GREY']], [COLORS['BLACK'], COLORS['GREY']], None])
    def test_order_create_with_colors(self, order_data, color):
        if color is not None:
            order_data['color'] = color
        
        response = OrderAPI.create_order(order_data)
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title('Можно совсем не указывать цвет')
    def test_order_create_without_color(self, order_data):
        response = OrderAPI.create_order(order_data)
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title('Тело ответа содержит track')
    def test_order_create_contains_track(self, order_data):
        response = OrderAPI.create_order(order_data)
        assert response.status_code == 201
        track = response.json().get('track')
        assert track is not None
        assert isinstance(track, int)