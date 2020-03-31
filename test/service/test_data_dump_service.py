import os, sys, unittest
#print(sys.path)
#sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from src.service.data_dump_service import *
from src.service.dolls_service import *

class TestDataDumpService(unittest.TestCase):
	def setUp(self):
		self.repository = DollsScrapingRepository()
			
	def test_yaml_dump(self):
		dd = DollsDump(self.repository, YamlDumper())
		dd.dump_file()
		self.assertTrue(os.path.exists('data/dolls_out.yaml'))

	def test_json_dump(self):
		dd = DollsDump(self.repository, JsonDumper())
		dd.dump_file()
		self.assertTrue(os.path.exists('data/dolls_out.json'))

if __name__ == '__main__':
	unittest.main()

