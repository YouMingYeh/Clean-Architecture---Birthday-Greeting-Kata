import unittest
from Repositories import MemoryMemberRepository, MySQLMemberRepository, MongoDBMemberRepository
from Generators import SimpleMessageGenerator
from Services import BirthdayService
from datetime import date
import json
import xml.etree.ElementTree as ET

class TestBirthdayService(unittest.TestCase):
    def setUp(self):
        self.repo = MongoDBMemberRepository()
        self.generator = SimpleMessageGenerator()
        self.service = BirthdayService(self.repo, self.generator)

    def test_send_greetings_json(self):
        res = self.service.send_greetings(today_date=date(1985, 8, 8), format="JSON")
        print(res)
        self.assertIsInstance(res, list)
        for message in res:
            self.assertIsInstance(message, str)
            try:
                json.loads(message)  # Try to parse the string as JSON
            except json.JSONDecodeError:
                self.fail(f"{message} is not valid JSON")
                
    def test_send_greetings_res_length(self):
        res = self.service.send_greetings(today_date=date(1985, 8, 8), format="XML")
        self.assertGreater(len(res), 0)

    def test_send_greetings_xml(self):
        res = self.service.send_greetings(today_date=date(1985, 8, 8), format="XML")
        print(res)
        self.assertIsInstance(res, list)
        for message in res:
            self.assertIsInstance(message, str)
            try:
                ET.fromstring(message)  # Try to parse the string as XML
            except ET.ParseError:
                self.fail(f"{message} is not valid XML")

if __name__ == '__main__':
    unittest.main()