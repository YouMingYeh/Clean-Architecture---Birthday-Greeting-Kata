from Entities import Greeting, Member

class SimpleMessageGenerator:
    def __init__(self):
        pass

    def generate(self, member: Member) -> Greeting:
        title = 'Subject: Happy Birthday!'
        content = f'Happy birthday, dear {member.first_name}!'
        return Greeting(title, content)