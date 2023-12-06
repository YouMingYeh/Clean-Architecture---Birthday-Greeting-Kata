import json
from dicttoxml import dicttoxml

class Greeting:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_xml(self):
        xml_string = dicttoxml(self.__dict__).decode()

        # Remove the XML declaration
        xml_string_without_declaration = xml_string.split('<?xml version="1.0" encoding="UTF-8" ?>')[1].strip()

        return xml_string_without_declaration
