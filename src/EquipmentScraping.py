# coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
import re
import datetime

def get_time(strtime):
	return datetime.datetime.strptime(strtime, '%H:%M')

class Equipment:
	def __init__(self, name, type, star, time):
		self.name = name
		self.type = type
		self.star = star
		try:
			self.time = get_time(time)
		except ValueError:
			self.time = get_time('00:00')

	def __repr__(self):
		return repr((self.name, self.type, self.star, self.time))

	def to_string(self):
		return '名前 : ' + self.name + '\n' \
			+ '種類 : ' + self.type + '\n' \
			+ 'レア度 : ' + self.star + '\n' \
			+ '製造時間 : {0}'.format(self.time.time()) + '\n\n'

class EquipmentScraping():
	def __init__(self):
		target_url = 'https://gamewith.jp/dollsfrontline/article/show/116374'
		html = urllib.request.urlopen(target_url).read()
		root = BeautifulSoup(html, 'html.parser')
		self.soup = root.find_all('div', {'class': 'df_weapon_table'})
		self.result = self.get_list()
	
	def create_equipment(self, key, element):
		equipment_content = element
		return Equipment(equipment_content.find_all('td')[1].get_text(), \
			key, \
			equipment_content.find_all('td')[0].get_text(), \
			equipment_content.find_all('td')[2].get_text())

	def get_list(self):
		equipment_list = []
		for k, v in self.create_dict().items():
			for eq in v:
				e = self.create_equipment(k, eq)
				print(e.to_string())
				equipment_list.append(e)
		return equipment_list

	def create_dict(self):
		equipments = self.soup[3:20]
		dict = {}
		dict['オプティカルサイト'] = equipments[0].find_all('tr')[1:5]
		dict["ホロサイト"] = equipments[1].find_all('tr')[1:5]
		dict["ドットサイト"] = equipments[2].find_all('tr')[1:5]
		dict["夜戦装備"] = equipments[3].find_all('tr')[1:5]
		dict["サイレンサー"] = equipments[4].find_all('tr')[1:5]
		dict["徹甲弾"] = equipments[5].find_all('tr')[1:5]
		dict["特殊弾"] = equipments[6].find_all('tr')[1:5]
		dict["高速弾"] = equipments[7].find_all('tr')[1:5]
		dict["散弾"] = equipments[8].find_all('tr')[1:9]
		dict["外骨格"] = equipments[9].find_all('tr')[1:9]
		dict["カモフラージュマント"] = equipments[10].find_all('tr')[1:5]
		dict["アサルトパック"] = equipments[11].find_all('tr')[1:3]
		dict["防弾ベスト"] = equipments[12].find_all('tr')[1:4]
		return dict

	def search(self, hour, minute):
		result_list = []
		for e in sorted(self.result, key=lambda e: e.time):
			input_time = get_time(str(hour) + ':' + str(minute))
			if (self.is_hit_search_policy(input_time, e)):
				result_list.append(e)
		return result_list

	def is_hit_search_policy(self, input_time, equipment):
		return abs(equipment.time - input_time).total_seconds() == 0

if __name__ == '__main__':
	es = EquipmentScraping()
	for e in es.result:
		print(e.to_string())

	for e in es.search(0, 58):
		print(e.to_string())

