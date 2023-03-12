import requests
from bs4 import BeautifulSoup
import json
from tgbot import get_new
from get_data import get_data

#Не работает. Не помню почему я забил, но может доделаю

def analiz():
    response = requests.get('https://freelance.habr.com/tasks?page=1&q=%D0%9F%D0%B0%D1%80%D1%81%D0%B5%D1%80')
    result = response.content

    soup = BeautifulSoup(result, 'lxml')

    first = soup.find(class_='task__title')

    link = first.find('a')

    link = 'https://freelance.habr.com/' + link.get('href')

    with open('works.json', encoding="utf-8") as file:
        works = json.load(file)

    if link == works[0]['url']:
        pass
    else:
        get_data()
        get_new()


def main():
    analiz()


if __name__ == '__main__':
    while True:
        main()