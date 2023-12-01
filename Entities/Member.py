from datetime import date

class Member:
    def __init__(self, first_name: str, last_name: str, gender: str, date_of_birth: date, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.email = email