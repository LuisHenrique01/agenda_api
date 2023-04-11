import unittest
from datetime import date
from uuid import UUID
from utils.personal import PersonalAgenda


class TestMock(unittest.TestCase):

    def setUp(self) -> None:
        self.event = {'name': 'estudar', 'endDate': date.today(),
                      'description': 'Estudar para o TCC'}
        return super().setUp()

    def test_a_get_list(self):
        expected_list = []
        self.assertEqual(PersonalAgenda.get_list(), expected_list)

    def test_b_create_event(self):
        new_event = PersonalAgenda.create_event(self.event)
        self.assertIsInstance(new_event.id, UUID)


if __name__ == '__main__':
    unittest.main()
