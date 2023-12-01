from Entities import Greeting, Member
from Repositories.Member import MemberRepository
from Generators import GreetingMessageGeneratorAbs

class BirthdayService:
    def __init__(self, repo: MemberRepository, generator: GreetingMessageGeneratorAbs):
        self.repo = repo
        self.generator = generator

    def send_greetings(self, format: str) -> str:
        member = self.repo.get_members_with_tody_birthday()
        greeting = self.generator.generate(member)

        if format == "JSON":
            return greeting.to_json()
        elif format == "XML":
            return greeting.to_xml()
        else:
            raise ValueError("Invalid format specified.")
