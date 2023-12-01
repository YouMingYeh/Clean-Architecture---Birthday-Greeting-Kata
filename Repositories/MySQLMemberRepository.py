from Entities import Member
from typing import List
from datetime import date
from Repositories.Member import MemberRepository

class MySQLMemberRepository(MemberRepository):
    def __init__(self):
        # TODO: Implement connection to MySQL Server
        self.today_date = date.today();
        pass;

    def add(self, member: Member):
        # TODO: Implement MySQL Insert
        pass;

    def get_all(self):
        # TODO: Implement MySQL Select
        pass;
    
    def get_members_with_tody_birthday(self):
        # TODO: Implement MySQL Select
        pass;
