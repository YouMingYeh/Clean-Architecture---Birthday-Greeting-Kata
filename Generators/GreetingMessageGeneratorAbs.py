from abc import ABC, abstractmethod
from Entities import Greeting, Member

# Create Greeting Generator Abstraction
class GreetingMessageGeneratorAbs(ABC):
    @abstractmethod
    def __init__(self):
       pass

    def generate(self, member: Member) -> Greeting:
        pass