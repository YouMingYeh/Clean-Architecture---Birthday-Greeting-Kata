from Entities import Greeting, Member
from Repositories.Member import MemberRepository
from Generators import GreetingMessageGeneratorAbs

class BirthdayService:
    def __init__(self, repo: MemberRepository, generator: GreetingMessageGeneratorAbs):
        self.repo = repo
        self.generator = generator

    def send_greetings(self, format: str) -> str:
        members = self.repo.get_all()
        greetings = []
        for member in members:
            greeting = self.generator.generate(member)
            if format == "JSON":
                greeting = greeting.to_json()
            elif format == "XML":
                greeting = greeting.to_xml()
            else:
                raise ValueError("Invalid format specified.")
            greetings.append(greeting)
        return greetings
        
