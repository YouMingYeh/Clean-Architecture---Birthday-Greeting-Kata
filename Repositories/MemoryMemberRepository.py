from Entities import Member
from typing import List
from datetime import date
from Repositories.Member import MemberRepository


class MemoryMemberRepository(MemberRepository):
    def __init__(self, today_date: date = date.today()):
        self.members = [
            Member(
                first_name="Robert",
                last_name="Yen",
                gender="Male",
                date_of_birth=date(1985, 8, 8),
                email="robert.yen@linecorp.com",
            ),
            Member(
                first_name="Cid",
                last_name="Change",
                gender="Male",
                date_of_birth=date(1990, 10, 10),
                email="cid.change@linecorp.com",
            ),
            Member(
                first_name="Miki",
                last_name="Lai",
                gender="Female",
                date_of_birth=date(1993, 4, 5),
                email="miki.lai@linecorp.com",
            ),
            Member(
                first_name="Sherry",
                last_name="Chen",
                gender="Female",
                date_of_birth=date(1993, 8, 8),
                email="sherry.lai@linecorp.com",
            ),
            Member(
                first_name="Peter",
                last_name="Wang",
                gender="Male",
                date_of_birth=date(1950, 12, 22),
                email="peter.wang@linecorp.com",
            ),
        ]
    def init_table(self):
        pass

    def add(self, member: Member):
        self.members.append(member)

    def get_all(self):
        return self.members

    def get_members_with_tody_birthday(self, today_date: date = date.today()):
        return [
            member
            for member in self.members
            if member.date_of_birth.day == today_date.day
            and member.date_of_birth.month == today_date.month
        ]
