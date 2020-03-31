import os, unittest
from src.service.data_dump_service import DollsDump, YamlDumper, JsonDumper
from src.service.dolls_service import DollsScrapingRepository


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
