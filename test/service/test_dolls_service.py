import os, sys, unittest
#print(sys.path)
#sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from src.service.dolls_service import *

class TestDollsService(unittest.TestCase):
	def setUp(self):
		self.scraping = DollsSearchService(DollsScrapingRepository())
		self.yaml = DollsSearchService(DollsYamlRepository())
	
	def test_scraping_result(self):
		for doll in self.scraping.repository.result:
			# 'name', 'type', 'star', 'time', 'link_url', 'how_to_get', 'image_url'
			self.assertIsNone(doll.name)
			self.assertIsNotNone(doll.type)
			self.assertIsNotNone(doll.star)
			self.assertIsNotNone(doll.time)
			self.assertIsNotNone(doll.link_url)
			self.assertIsNotNone(doll.how_to_get)
			self.assertIsNotNone(doll.image_url)

	def test_yaml_result(self):
		for doll in self.yaml.repository.result:
			# 'name', 'type', 'star', 'time', 'link_url', 'how_to_get', 'image_url'
			self.assertIsNotNone(doll.name)
			self.assertIsNotNone(doll.type)
			self.assertIsNotNone(doll.star)
			self.assertIsNotNone(doll.time)
			self.assertIsNotNone(doll.link_url)
			self.assertIsNotNone(doll.how_to_get)
			self.assertIsNotNone(doll.image_url)

if __name__ == '__main__':
	unittest.main()
