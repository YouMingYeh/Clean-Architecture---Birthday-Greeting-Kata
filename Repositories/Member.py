# 3. Define Repository: Member Repository
from Entities import Member
from typing import List
from datetime import date
from abc import ABC, abstractmethod

class MemberRepository(ABC):
    @abstractmethod
    def __init__(self):
        pass;

    def add(self, member: Member):
        pass;

    def get_all(self):
        pass;
    
    def get_members_with_tody_birthday(self, today_date: date):
        pass;