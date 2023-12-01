import unittest
from Entities import Member
from datetime import datetime
from Repositories.MongoDBMemberRepository import MongoDBMemberRepository

class TestMongoDBMemberRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MongoDBMemberRepository()

    def test_add(self):
        member = Member(first_name="John", last_name="Doe", date_of_birth=datetime.now(), gender='Male', email="test@test.com")
        self.repo.add(member)

        # Verify that the member was added to the collection
        members = self.repo.get_all()
        print(members[0].__dict__)

    def test_get_all(self):
        # Add a member to the collection
        member = Member(first_name="John", last_name="Doe", date_of_birth=datetime.now(), gender='Male', email="test@test.com")
        self.repo.add(member)

        # Verify that get_all returns the added member
        members = self.repo.get_all()
        print(members[0].__dict__)

    def test_get_members_with_tody_birthday(self):
        # Add a member with today's birthday to the collection
        member = Member(first_name="John", last_name="Doe", date_of_birth=datetime.now(), gender='Male', email="test@test.com")
        self.repo.add(member)

        # Verify that get_members_with_tody_birthday returns the added member
        members = self.repo.get_members_with_tody_birthday()
        # print(members[0].__dict__)

if __name__ == '__main__':
    unittest.main()