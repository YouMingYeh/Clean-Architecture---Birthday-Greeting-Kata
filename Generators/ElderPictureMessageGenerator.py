from Entities import Greeting, Member
from typing import List
from Generators import GreetingMessageGeneratorAbs

class ElderPictureMessageGenerator(GreetingMessageGeneratorAbs):
    def __init__(self, picture_path: str):
        self.picture_path = picture_path

    def generate(self, member: Member) -> Greeting:
        title = 'Subject: Happy Birthday!\n'
        content = f'Happy birthday, dear {member.first_name}!\n'
        if member.age >= 49:
            content += self.picture_path
        return Greeting(title, content)
        