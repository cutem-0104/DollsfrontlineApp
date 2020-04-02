# coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
import datetime
from typing import NamedTuple


# Doll = namedtuple('Doll', (
#     'name', 'type', 'star', 'time', 'link_url', 'how_to_get', 'image_url'))
class Doll(NamedTuple):
    name: str
    type: str
    star: str
    time: int
    link_url: str
    how_to_get: str
    image_url: str


def get_time(strtime):
    try:
        time = datetime.datetime.strptime(strtime, '%H:%M')
        return time.hour * 60 + time.minute
    except ValueError:
        return 0


class DollsScrapingRepository():
    def __init__(self):
        target_url = 'https://gamewith.jp/dollsfrontline/article/show/115648'
        html = urllib.request.urlopen(target_url).read()
        root = BeautifulSoup(html, 'html.parser')
        self.soup = root.find_all('section', {'class': 'w-idb-element'}, 'td')
        self.result = self.get_list()

    def create_doll(self, element):
        doll_content = element.find_all('td')

        return Doll(doll_content[0].get_text(),
                    self.get_gun_type(doll_content[1].get_text()),
                    doll_content[2].get_text(),
                    get_time(doll_content[15].get_text()),
                    doll_content[0].a.attrs['href'],
                    doll_content[16].get_text(),
                    doll_content[0].img.attrs['data-original'])

    def get_list(self):
        doll_list = []
        for doll_element in self.soup:
            doll_list.append(self.create_doll(doll_element))
        return doll_list

    def get_gun_type(self, gun_type):
        if gun_type == 'アサルトライフル':
            return 'AR'
        elif gun_type == 'サブマシンガン':
            return 'SMG'
        elif gun_type == 'ライフル':
            return 'RF'
        elif gun_type == 'マシンガン':
            return 'MG'
        elif gun_type == 'ショットガン':
            return 'SG'
        elif gun_type == 'ハンドガン':
            return 'HG'


class DollsYamlRepository():
    def __init__(self):
        self.result = self.load()

    def load(self):
        import yaml

        with open('data/dolls_out.yaml') as file:
            return yaml.load(file)


class DollsSearchService():
    def __init__(self, repository):
        self.repository = repository

    def search(self, hour, minute, star, gun_type):
        result_list = []
        for d in self.repository.result:
            if (self.is_hit_search_policy(hour, minute, star, gun_type, d)):
                result_list.append(d)
        return result_list

    def is_hit_search_policy(self, hour, minute, star, gun_type, doll):
        equal_star = True
        if (star != '-'):
            equal_star = star == doll.star

        equal_time = True
        if (hour != '-'):
            input_time = int(hour) * 60 + int(minute)
            equal_time = abs(doll.time - input_time) == 0

        equal_type = True
        if (gun_type != '-'):
            equal_type = gun_type == doll.type
        return equal_time and equal_star and equal_type


if __name__ == '__main__':
    ds_service = DollsSearchService(DollsYamlRepository())
    # ds_service = DollsSearchService(DollsYamlRepository())
    for d in ds_service.repository.result:
        print(d)
