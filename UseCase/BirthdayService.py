from Entities import Greeting, Member
from Repositories.Member import MemberRepository
from UseCase.GreetingMessageGenerator import GreetingMessageGenerator

class BirthdayService:
    def __init__(self, repo: MemberRepository, generator: GreetingMessageGenerator):
        self.repo = repo
        self.generator = generator

    def send_greetings(self) -> Greeting:
        member = self.repo.get_members_with_tody_birthday()
        greeting = self.generator.generate(member)
        return greeting