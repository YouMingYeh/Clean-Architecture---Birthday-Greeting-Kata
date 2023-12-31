from Entities import Greeting, Member
from .GreetingMessageGeneratorAbs import GreetingMessageGeneratorAbs

class SimpleMessageWithFullNameGenerator(GreetingMessageGeneratorAbs):
    def __init__(self):
        pass

    def generate(self, member: Member) -> Greeting:
        title = 'Subject: Happy Birthday!\n'
        content = f'Happy birthday, dear {member.last_name}, {member.first_name}!\n'
        return Greeting(title, content)