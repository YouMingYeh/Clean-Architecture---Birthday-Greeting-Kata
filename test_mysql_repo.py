import unittest
from datetime import date
from Repositories import MySQLMemberRepository
from Entities import Member

class TestMySQLMemberRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MySQLMemberRepository()
        self.repo.init_table()

    def test_get_all(self):
        members = self.repo.get_all()
        self.assertIsInstance(members, list)
        self.assertTrue(all(isinstance(m, Member) for m in members))

    def test_get_members_with_tody_birthday(self):
        members = self.repo.get_members_with_tody_birthday()
        self.assertIsInstance(members, list)
        self.assertTrue(all(isinstance(m, Member) for m in members))
        self.assertTrue(all(m.date_of_birth.month == date.today().month and m.date_of_birth.day == date.today().day for m in members))
        
    def tearDown(self):
        self.repo.drop_table()

if __name__ == '__main__':
    unittest.main()