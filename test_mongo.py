import unittest
import dotenv
import os
from pymongo.mongo_client import MongoClient
from Entities import Member
from datetime import datetime

dotenv.load_dotenv()

class TestMongoConnection(unittest.TestCase):
    def test_connection(self):
        client = MongoClient(os.getenv("MONGO_URI"))
        try: 
            client.admin.command('ping')
            db = client["CA"]
            collection = db["member"]
            # Insert a member to the collection
            new_member = Member(
                first_name="Robert",
                last_name="Yen",
                gender="Male",
                date_of_birth=datetime(1985, 8, 8),
                email="robert.yen@linecorp.com",
            )
            collection.insert_one(new_member.__dict__)
            # Read the member from the collection
            member = collection.find_one(new_member.__dict__)
            test = Member(
                first_name=member['first_name'],
                last_name=member['last_name'],
                gender=member['gender'],
                date_of_birth=member['date_of_birth'],
                email=member['email'],
            )
            print(test.__dict__)

            # Delete the member from the collection
            collection.delete_one(member)

        except:
            self.fail("Connection to MongoDB failed")


if __name__ == '__main__':
    unittest.main()