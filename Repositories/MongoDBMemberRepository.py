from Entities import Member
from typing import List
from datetime import date
from Repositories.Member import MemberRepository
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


class MongoDBMemberRepository(MemberRepository):
    def __init__(self):
        # TODO: Implement connection to MongoDB Server
        self.today_date = date.today()
        load_dotenv()
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client["CA"]
        self.collection = self.db["member"]

    def add(self, member: Member):
        # TODO: Implement MongoDB Insert
        self.collection.insert_one(member.__dict__)

    def get_all(self):
        # TODO: Implement MongoDB Select
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

    def get_members_with_tody_birthday(self):
        # TODO: Implement MongoDB Select
        today = self.today_date.strftime("%m-%d")
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
