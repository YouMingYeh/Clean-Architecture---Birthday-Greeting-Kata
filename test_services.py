import unittest
from datetime import date
from Services.BirthdayService import BirthdayService
from Repositories.MemoryMemberRepository import MemoryMemberRepository
from Generators.SimpleMessageGenerator import SimpleMessageGenerator

class TestBirthdayService(unittest.TestCase):
    def setUp(self):
        self.member_repository = MemoryMemberRepository()
        self.message_generator = SimpleMessageGenerator()
        self.birthday_service = BirthdayService(self.member_repository, self.message_generator)

    def test_send_greetings(self):
        # Assuming BirthdayService.send_greetings returns a list of messages sent
        messages = self.birthday_service.send_greetings("XML")
        print(messages)
        # Add more assertions based on your specific requirements

if __name__ == '__main__':
    unittest.main()