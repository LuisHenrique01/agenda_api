import unittest
from datetime import date
from utils.mock import Mock


class TestMock(unittest.TestCase):

    def test_get_list(self):
        expected_list = [{'id': 1, 'name': 'estudar',
                          'endDate': date.today(),
                          'description': 'Estudar para o TCC'}]
        self.assertEqual(Mock.get_list(), expected_list)


if __name__ == '__main__':
    unittest.main()
