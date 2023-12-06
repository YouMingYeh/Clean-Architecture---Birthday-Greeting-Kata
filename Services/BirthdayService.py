from Entities import Greeting, Member
from Repositories.Member import MemberRepository
from Generators import GreetingMessageGeneratorAbs

class BirthdayService:
    def __init__(self, repo: MemberRepository, generator: GreetingMessageGeneratorAbs):
        self.repo = repo
        self.repo.init_table()
        self.generator = generator

    def send_greetings(self, format: str):
        members = self.repo.get_members_with_tody_birthday()
        greetings = []
        for member in members:
            greeting = self.generator.generate(member)
            greetings.append(greeting)

        if format == "JSON":
            for greeting in greetings:
                greeting.to_json()
        elif format == "XML":
            for greeting in greetings:
                greeting.to_xml()
        else:
            raise ValueError("Invalid format specified.")
        
        # parse the greetings(Greeting[]) to JSON or XML
        
        return greetings
