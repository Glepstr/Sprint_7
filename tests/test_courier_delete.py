import pytest
import allure
from api.courier_api import CourierAPI
from data import ERROR_MESSAGES

@allure.feature('Курьер')
@allure.story('Удаление курьера')
class TestCourierDelete:
    
    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self, create_courier):
        login, password, _ = create_courier
        courier_id = CourierAPI.get_courier_id(login, password)
        
        response = CourierAPI.delete_courier(courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}
    
    @allure.title('Ошибка при удалении с несуществующим id')
    def test_delete_courier_invalid_id(self):
        response = CourierAPI.delete_courier(999999)
        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['COURIER_DELETE_NOT_FOUND']