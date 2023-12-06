from Entities import Member
from typing import List
from datetime import date, datetime
from Repositories.Member import MemberRepository
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


class MongoDBMemberRepository(MemberRepository):
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client["CA"]
        self.collection = self.db["member"]

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

    def add(self, member: Member):
        member_dict = member.__dict__
        member_dict["date_of_birth"] = datetime.combine(member_dict["date_of_birth"], datetime.min.time())
        self.collection.insert_one(member_dict)

    def init_table(self):
        members_dict = [member.__dict__ for member in self.members]
        for member_dict in members_dict:
            member_dict["date_of_birth"] = datetime.combine(member_dict["date_of_birth"], datetime.min.time())
        self.collection.insert_many(members_dict)

    def drop_table(self):
        self.collection.drop()

    def get_all(self):
        members = self.collection.find()
        members = [
            Member(
                first_name=member['first_name'],
                last_name=member['last_name'],
                gender=member['gender'],
                date_of_birth=member['date_of_birth'],
                email=member['email'],
            )
            for member in members
        ]
        return members

    def get_members_with_tody_birthday(self, today_date: date = date.today()):
        today = today_date.strftime("%m-%d")
        members = self.collection.find({"date_to_birth": today})
        members = [
            Member(
                first_name=member['first_name'],
                last_name=member['last_name'],
                gender=member['gender'],
                date_of_birth=member['date_of_birth'],
                email=member['email'],
            )
            for member in members
        ]
        return members
