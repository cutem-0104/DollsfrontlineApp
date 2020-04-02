import unittest
from src.service.dataaccess_service import MySqlService


class TestMysqlService(unittest.TestCase):
    def test_mysql_connection(self):
        self.assertTrue(MySqlService().is_connected())

    def test_select_all(self):
        result = MySqlService().select_all()
        for d in result:
            self.assertIsNotNone(d.name)

    def test_select_count(self):
        count = MySqlService().select_count()[0]
        print(count)
        self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()
