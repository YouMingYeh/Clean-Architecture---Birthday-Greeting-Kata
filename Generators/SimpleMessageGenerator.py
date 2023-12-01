from Entities import Greeting, Member
from Generators import GreetingMessageGeneratorAbs 

class SimpleMessageGenerator(GreetingMessageGeneratorAbs):
    def __init__(self):
        pass

    def generate(self, member: Member) -> Greeting:
        title = 'Subject: Happy Birthday!\n'
        content = f'Happy birthday, dear {member.first_name}!\n'
        return Greeting(title, content)