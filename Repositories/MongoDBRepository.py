from Entities import Member
from typing import List
from datetime import date
from Repositories.Member import MemberRepository

class MongoDBMemberRepository(MemberRepository):
    def __init__(self):
        # TODO: Implement connection to MongoDB Server
        self.today_date = date.today();
        pass;

    def add(self, member: Member):
        # TODO: Implement MongoDB Insert
        pass;

    def get_all(self):
        # TODO: Implement MongoDB Select
        pass;
    
    def get_members_with_tody_birthday(self):
        # TODO: Implement MongoDB Select
        pass;
