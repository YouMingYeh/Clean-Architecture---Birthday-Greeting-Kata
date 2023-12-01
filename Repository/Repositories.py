# 3. Define Repository: Member Repository
from Entity.Entities import Member
from typing import List

class MemberRepository:
    def __init__(self, members: List[Member]):
        self.members = members

    def add(self, member: Member):
        self.members.append(member)

    def get_all(self):
        return self.members