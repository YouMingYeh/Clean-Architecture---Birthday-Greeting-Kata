import unittest
from datetime import date
from Entities import Member, Greeting

class TestEntities(unittest.TestCase):
    def test_member(self):
        member = Member('John', 'Doe', 'Male', date(1990, 1, 1), 'john.doe@example.com')
        self.assertEqual(member.first_name, 'John')
        self.assertEqual(member.last_name, 'Doe')
        self.assertEqual(member.gender, 'Male')
        self.assertEqual(member.date_of_birth, date(1990, 1, 1))
        self.assertEqual(member.email, 'john.doe@example.com')

    def test_greeting(self):
        greeting = Greeting('Hello', 'World')
        self.assertEqual(greeting.title, 'Hello')
        self.assertEqual(greeting.content, 'World')

if __name__ == '__main__':
    unittest.main()