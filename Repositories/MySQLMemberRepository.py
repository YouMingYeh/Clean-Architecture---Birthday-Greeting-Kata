from Entities import Member
from typing import List
from datetime import date
from Repositories.Member import MemberRepository
import mysql.connector
from dotenv import load_dotenv
import os

from Entities import Member


class MySQLMemberRepository(MemberRepository):
    def __init__(self):
        load_dotenv()
        self.db = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
        )

        self.cursor = self.db.cursor()

    def drop_table(self):
        self.cursor.execute("""
            DROP TABLE IF EXISTS members
        """)
        self.db.commit()
        
    def init_table(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            gender VARCHAR(255) NOT NULL,
            date_of_birth DATE NOT NULL,
            email VARCHAR(255) NOT NULL
        )             
                """
        )

        # Insert the members into the table
        members = [
            ("Robert", "Yen", "Male", date(1985, 8, 8), "robert.yen@linecorp.com"),
            ("Cid", "Change", "Male", date(1990, 10, 10), "cid.change@linecorp.com"),
            ("Miki", "Lai", "Female", date(1993, 4, 5), "miki.lai@linecorp.com"),
            ("Sherry", "Chen", "Female", date(1993, 8, 8), "sherry.lai@linecorp.com"),
            ("Peter", "Wang", "Male", date(1950, 12, 22), "peter.wang@linecorp.com"),
        ]

        self.cursor.executemany(
            """
            INSERT INTO members (first_name, last_name, gender, date_of_birth, email)
            VALUES (%s, %s, %s, %s, %s)
        """,
            members,
        )

        self.db.commit()

    def add(self, member: Member):

        pass

    def get_all(self):
        self.cursor.execute("SELECT * FROM members")
        members = []
        for row in self.cursor.fetchall():
            member = Member(
                first_name=row[1],
                last_name=row[2],
                gender=row[3],
                date_of_birth=row[4],
                email=row[5],
            )
            members.append(member)
        return members

    def get_members_with_tody_birthday(self, today_date: date = date.today()):
        self.cursor.execute(
            "SELECT * FROM members WHERE MONTH(date_of_birth) = %s AND DAY(date_of_birth) = %s",
            (today_date.month, today_date.day),
        )
        members = []
        for row in self.cursor.fetchall():
            member = Member(
                first_name=row[1],
                last_name=row[2],
                gender=row[3],
                date_of_birth=row[4],
                email=row[5],
            )
            members.append(member)
        return members
