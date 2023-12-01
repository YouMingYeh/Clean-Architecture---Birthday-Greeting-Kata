from datetime import date
from email import email

# 1. Define member entity
class Member:
    def __init__(self, first_name: str, last_name: str, gender: str, date_of_birth: date, email: email):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.email = email

# 2. Define Greeting entity
class Greeting:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content