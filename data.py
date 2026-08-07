# data.py
BASE_URL = 'https://qa-scooter.praktikum-services.ru'

# Эндпоинты
COURIER_ENDPOINT = '/api/v1/courier'
COURIER_LOGIN_ENDPOINT = '/api/v1/courier/login'
COURIER_DELETE_ENDPOINT = '/api/v1/courier/{}'
ORDER_ENDPOINT = '/api/v1/orders'
ORDER_TRACK_ENDPOINT = '/api/v1/orders/track'
ORDER_ACCEPT_ENDPOINT = '/api/v1/orders/accept/{}'

# Цвета
COLORS = {
    'BLACK': 'BLACK',
    'GREY': 'GREY'
}

# Базовые данные для заказа
ORDER_DATA = {
    "firstName": "Test",
    "lastName": "User",
    "address": "Test Address 123",
    "metroStation": 4,
    "phone": "+79999999999",
    "rentTime": 5,
    "deliveryDate": "2024-12-31",
    "comment": "Test comment"
}

# Сообщения об ошибках
ERROR_MESSAGES = {
    'COURIER_CREATE_MISSING_FIELD': 'Недостаточно данных для создания учетной записи',
    'COURIER_CREATE_EXIST': 'Этот логин уже используется. Попробуйте другой.',
    'COURIER_LOGIN_MISSING_FIELD': 'Недостаточно данных для входа',
    'COURIER_LOGIN_INVALID': 'Учетная запись не найдена',
    'COURIER_DELETE_NOT_FOUND': 'Курьера с таким id нет.',
    'ORDER_ACCEPT_INVALID_COURIER': 'Курьера с таким id не существует',
    'ORDER_TRACK_MISSING_NUMBER': 'Недостаточно данных для поиска',
    'ORDER_TRACK_NOT_FOUND': 'Заказ не найден'
}