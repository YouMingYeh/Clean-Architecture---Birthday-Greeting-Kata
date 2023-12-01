from Entities import Greeting, Member
from typing import List
from UseCase.GreetingMessageGenerator import GreetingMessageGenerator

class TailerMadeMessageGenerator(GreetingMessageGenerator):
    def __init__(self, discount_for_male: int, items_for_male: List[str], discount_for_female: int, items_for_female: List[str]):
        self.discount_for_male = discount_for_male
        self.items_for_male = items_for_male
        self.discount_for_female = discount_for_female
        self.items_for_female = items_for_female

    def generate(self, member: Member) -> Greeting:
        title = 'Subject: Happy Birthday!\n'
        content = f'Happy birthday, dear {member.first_name}!\n'
        if member.gender == "Male":
            content += f'We offer special discount {self.discount_for_male}% off for the following items:\n'
            content += '\n'.join(self.items_for_male)
        elif member.gender == "Female":
            content += f'We offer special discount {self.discount_for_female}% off for the following items:\n'
            content += '\n'.join(self.items_for_female)
        return Greeting(title, content)
        