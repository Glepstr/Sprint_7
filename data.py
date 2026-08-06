import allure

BASE_URL = 'https://qa-scooter.praktikum-services.ru'

# Эндпоинты для курьеров
COURIER_ENDPOINT = '/api/v1/courier'
COURIER_LOGIN_ENDPOINT = '/api/v1/courier/login'
COURIER_DELETE_ENDPOINT = '/api/v1/courier/{}'

# Эндпоинты для заказов
ORDER_ENDPOINT = '/api/v1/orders'
ORDER_TRACK_ENDPOINT = '/api/v1/orders/track'
ORDER_ACCEPT_ENDPOINT = '/api/v1/orders/accept/{}'

# Цвета для заказа
COLORS = {
    'BLACK': 'BLACK',
    'GREY': 'GREY',
    'NONE': None
}

# Сообщения об ошибках
ERROR_MESSAGES = {
    'COURIER_CREATE_MISSING_FIELD': 'Недостаточно данных для создания учетной записи',
    'COURIER_CREATE_EXIST': 'Этот логин уже используется. Попробуйте другой.',
    'COURIER_LOGIN_MISSING_FIELD': 'Недостаточно данных для входа',
    'COURIER_LOGIN_INVALID': 'Учетная запись не найдена',
    'COURIER_DELETE_MISSING_ID': 'Недостаточно данных для удаления курьера',
    'COURIER_DELETE_NOT_FOUND': 'Курьера с таким id нет.',
    'ORDER_ACCEPT_MISSING_COURIER': 'Недостаточно данных для принятия заказа',
    'ORDER_ACCEPT_INVALID_COURIER': 'Курьера с таким id не существует',
    'ORDER_ACCEPT_INVALID_ORDER': 'Заказа с таким id не существует',
    'ORDER_TRACK_MISSING_NUMBER': 'Недостаточно данных для поиска',
    'ORDER_TRACK_NOT_FOUND': 'Заказ не найден'
}