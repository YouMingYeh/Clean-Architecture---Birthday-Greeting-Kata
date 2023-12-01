import unittest
from Generators import ElderPictureMessageGenerator, SimpleMessageWithFullNameGenerator, SimpleMessageGenerator, TailerMadeMessageGenerator
from Entities.Member import Member
from datetime import date

class TestGenerators(unittest.TestCase):
    def setUp(self):
        self.member = Member('John', 'Doe', 'Male', date(1990, 1, 1), 'john.doe@example.com')

    def test_simple_message_generator(self):
        generator = SimpleMessageGenerator()
        greeting = generator.generate(self.member)
        self.assertEqual(greeting.title, 'Subject: Happy Birthday!\n')
        self.assertEqual(greeting.content, 'Happy birthday, dear John!\n')

    def test_simple_message_with_full_name_generator(self):
        generator = SimpleMessageWithFullNameGenerator()
        greeting = generator.generate(self.member)
        self.assertEqual(greeting.title, 'Subject: Happy Birthday!\n')
        self.assertEqual(greeting.content, 'Happy birthday, dear Doe, John!\n')

    def test_elder_picture_message_generator(self):
        generator = ElderPictureMessageGenerator('/path/to/picture')
        greeting = generator.generate(self.member)
        self.assertEqual(greeting.title, 'Subject: Happy Birthday!\n')
        self.assertEqual(greeting.content, 'Happy birthday, dear John!\n')

    def test_tailer_made_message_generator(self):
        generator = TailerMadeMessageGenerator(10, ['item1', 'item2'], 20, ['item3', 'item4'])
        greeting = generator.generate(self.member)
        self.assertEqual(greeting.title, 'Subject: Happy Birthday!\n')
        self.assertTrue('Happy birthday, dear John!\n' in greeting.content)
        self.assertTrue('We offer special discount 10% off for the following items:\n' in greeting.content)
        self.assertTrue('item1\nitem2' in greeting.content)

if __name__ == '__main__':
    unittest.main()