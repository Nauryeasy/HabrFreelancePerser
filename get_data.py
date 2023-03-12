import requests
from bs4 import BeautifulSoup
import lxml
import json


def get_data():
    works = []

    links = []

    response = requests.get('https://freelance.habr.com/tasks?page=1&q=%D0%9F%D0%B0%D1%80%D1%81%D0%B5%D1%80')
    result = response.content

    soup = BeautifulSoup(result, 'lxml')

    class_for_links = soup.find_all(class_='task__title')

    for object in class_for_links:
        link = object.find('a')

        links.append(link.get('href'))
    for link in links:
        url = 'https://freelance.habr.com/' + link
        q = requests.get(url)
        result_q = q.content

        soup_q = BeautifulSoup(result_q, 'lxml')

        name = soup_q.find(class_='task__title').getText()
        price = soup_q.find(class_='count').getText()
        date = soup_q.find(class_='task__meta').getText()
        tz = soup_q.find(class_='task__description').getText()

        works.append(
            {
                'name': name,
                'price': price,
                'date': date,
                'tz': tz,
                'url': url
            }
        )

    with open('works.json', 'w', encoding="utf-8") as file:
        json.dump(works, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()