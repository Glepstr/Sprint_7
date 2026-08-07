import pytest
import allure
from data import COLORS, ORDER_DATA
from api.order_api import OrderAPI

@allure.feature('Заказ')
@allure.story('Создание заказа')
class TestOrderCreate:
    
    @allure.title('Можно указать цвет BLACK')
    def test_order_create_black_color(self):
        order_data = ORDER_DATA.copy()
        order_data['color'] = [COLORS['BLACK']]
        
        response = OrderAPI.create_order(order_data)
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title('Можно указать цвет GREY')
    def test_order_create_grey_color(self):
        order_data = ORDER_DATA.copy()
        order_data['color'] = [COLORS['GREY']]
        
        response = OrderAPI.create_order(order_data)
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title('Можно указать оба цвета')
    def test_order_create_both_colors(self):
        order_data = ORDER_DATA.copy()
        order_data['color'] = [COLORS['BLACK'], COLORS['GREY']]
        
        response = OrderAPI.create_order(order_data)
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title('Можно совсем не указывать цвет')
    def test_order_create_without_color(self):
        order_data = ORDER_DATA.copy()
        
        response = OrderAPI.create_order(order_data)
        assert response.status_code == 201
        assert 'track' in response.json()