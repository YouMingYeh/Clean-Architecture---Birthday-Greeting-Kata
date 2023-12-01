from Entities import Greeting, Member

class SimpleMessageGenerator:
    def __init__(self):
        pass

    def generate(self, member: Member) -> Greeting:
        title = 'Subject: Happy Birthday!\n'
        content = f'Happy birthday, dear {member.first_name}!\n'
        return Greeting(title, content)