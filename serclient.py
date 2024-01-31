import requests
import asyncio
import aiohttp

with open("env/data/link.txt", "r", encoding="utf-8") as file:
    for line in file:
        urlServer = str(line.strip())


# Отправка числа в API для записи в файл
def send_number_to_api(number, iduser):
    url = f'{urlServer}/write_number'
    data = {'number': number, 'iduser': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response)
    if response.status_code == 200:
        print('Number has been sent to the API and written to the file')
    else:
        print('Failed to send the number to the API')


def can(iduser):
    url = f'{urlServer}/can'
    data = {'nick': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())
    if response.status_code == 200 and response.json()["can"]:
        return True
    elif response.status_code == 200:
        return False
    else:
        return False


async def top():
    url = f'{urlServer}/top'
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            if response.status == 200:
                data = await response.json()
                return data["top"].split("lol")
            else:
                return ["can'tLoad data",'1 данные']


def result(nick):
    data = {"nick": nick}
    response = requests.post(f"{urlServer}/myresult", json=data)
    if response.status_code == 200:
        return response.json()["result"]


async def mest(nick):
    data = {"iduser": nick}
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{urlServer}/mesto", json=data) as response:
            if response.status == 200:
                response_json = await response.json()
                return await wksajdbksaj(response_json['index'])
            else:
                return "-1"


async def wksajdbksaj(number):
    if number == 1:
        return f"{number}st"
    elif number == 2:
        return f"{number}nd"
    elif number == 3:
        return f"{number}rd"
    else:
        return f"{number}th"


def getMesto(nick):
    result = asyncio.run(mest(nick))
    return result
