from Entities import Greeting, Member
from typing import List
from .GreetingMessageGeneratorAbs import GreetingMessageGeneratorAbs
from datetime import date

class ElderPictureMessageGenerator(GreetingMessageGeneratorAbs):
    def __init__(self, picture_path: str):
        self.picture_path = picture_path

    def generate(self, member: Member) -> Greeting:
        title = 'Subject: Happy Birthday!\n'
        content = f'Happy birthday, dear {member.first_name}!\n'
        if date.today().year - member.date_of_birth.year >=50:
            return Greeting(title, content, self.picture_path)
        
        return Greeting(title, content)
        