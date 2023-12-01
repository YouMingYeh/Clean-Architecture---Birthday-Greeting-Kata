from Entities import Member
from typing import List
from datetime import date
from Repositories.Member import MemberRepository

class SQLMemberRepository(MemberRepository):
    def __init__(self):
        # TODO: Implement connection to SQL Server
        pass;

    def add(self, member: Member):
        # TODO: Implement SQL Insert
        pass;

    def get_all(self):
        # TODO: Implement SQL Select
        pass;
    
    def get_members_with_tody_birthday(self, today_date: date):
        # TODO: Implement SQL Select
        pass;
