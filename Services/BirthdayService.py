
from Repositories.Member import MemberRepository
from Generators import GreetingMessageGeneratorAbs
from datetime import date

class BirthdayService:
    def __init__(self, repo: MemberRepository, generator: GreetingMessageGeneratorAbs):
        self.repo = repo
        self.repo.init_table()
        self.generator = generator

    def send_greetings(self, today_date: date = date.today(), format: str = "JSON"):
        members = self.repo.get_members_with_tody_birthday(today_date)
        greetings = []
        for member in members:
            greeting = self.generator.generate(member)
            

            if format == "JSON":
                greeting = greeting.to_json()
                greetings.append(greeting)
            elif format == "XML":
                greeting = greeting.to_xml()
                greetings.append(greeting)
            else:
                raise ValueError("Invalid format specified.")
        
        # parse the greetings(Greeting[]) to JSON or XML
        
        return greetings
