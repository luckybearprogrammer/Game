

# Получаем текущее местоположение
import requests

# Делаем запрос к сайту для определения IP-адреса
response = requests.get('https://api.ipify.org?format=json')

# Парсим JSON ответ
ip_address = response.json()['ip']

# Делаем запрос к ipinfo.io
response = requests.get('https://ipinfo.io/' + ip_address + '/json')

# Парсим JSON ответ
data = response.json()
coordinates = list(map(float, data['loc'].split(',')))

API_KEY = '4e4b0a737dea8c94d94d9ebe6ecbd75b'  # Замените на ваш собственный ключ API


# Функция для получения данных о погоде на основе текущей геолокации
def get_current_weather():
    # Получаем текущие координаты пользователя (например, через geolocation API браузера)
    latitude = coordinates[0]
    longitude = coordinates[1]  # Например, координаты Москвы

    # Формируем запрос к OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{temperature}°С"
    else:
        print('Не удалось получить данные о погоде')

# get_current_weather()
# Используем функцию для получения данных о текущей погоде

