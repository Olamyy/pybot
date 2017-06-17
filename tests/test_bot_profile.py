import unittest
from unittest import mock
from core.core import PyBotProfile


class BotProfileTest(unittest.TestCase):
    def setUp(self):
        self.profile = PyBotProfile(name='Olamilekan')
        self.getattribute = 'name'
        self.setattribute = {'nationality': 'Nigeria'}

    def tearDown(self):
        pass

    def test_get_bot_details(self):
        output = self.profile.get_attribute(self.getattribute)
        self.assertEqual(self.profile.name, output)

    def test_set_bot_details(self):
        output = self.profile.set_attribute(list(self.setattribute.keys())[0], list(self.setattribute.values())[0])
        self.assertEqual(list(self.setattribute.values())[0], output)

if __name__ == '__main__':
    unittest.main()
