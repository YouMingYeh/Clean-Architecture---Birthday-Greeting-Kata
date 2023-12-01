import json
from dicttoxml import dicttoxml

class Greeting:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_xml(self):
        return dicttoxml(self.__dict__).decode()