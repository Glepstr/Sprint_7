import allure
from api.order_api import OrderAPI

@allure.feature('Заказ')
@allure.story('Список заказов')
class TestOrderList:
    
    @allure.title('В тело ответа возвращается список заказов')
    def test_order_list_returns_list(self):
        response = OrderAPI.get_orders()
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)