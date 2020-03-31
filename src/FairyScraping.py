# coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
import re
import datetime

def get_time(strtime):
	return datetime.datetime.strptime(strtime, '%H:%M')

class Fairy:
	def __init__(self, name, time):
		self.name = name
		try:
			self.time = get_time(time)
		except ValueError:
			self.time = get_time('00:00')

	def __repr__(self):
		return repr((self.name, self.time))

	def to_string(self):
		return '名前 : ' + self.name + '\n' \
			+ '製造時間 : {0}'.format(self.time.time()) + '\n\n'

class FairyScraping():
	def __init__(self):
		target_url = 'https://gamewith.jp/dollsfrontline/article/show/145926'
		html = urllib.request.urlopen(target_url).read()
		root = BeautifulSoup(html, 'html.parser')
		self.soup = root.find_all('table')
		self.result = self.get_list()
	
	def create_fairy(element):
		return Fairy(element.find_all('td')[0].get_text(), \
			element.find_all('td')[14].get_text())

	def get_list(self):
		fairy_list = []
		for f in self.soup[10:30]:
			fairy = FairyScraping.create_fairy(f)
			fairy_list.append(fairy)
		return fairy_list

	def search(self, hour, minute):
		result_list = []
		for fairy in sorted(self.result, key=lambda f: f.time):
			input_time = get_time(str(hour) + ':' + str(minute))
			if (self.is_hit_search_policy(input_time, fairy)):
				result_list.append(fairy)
		return result_list

	def is_hit_search_policy(self, input_time, fairy):
		return abs(fairy.time - input_time).total_seconds() == 0

if __name__ == '__main__':
	fs = FairyScraping()
	for f in fs.result:
		print(f.to_string())

	for f in fs.search_fairy(3, 00):
		print(f.to_string())
