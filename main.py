from flask import Flask, jsonify, request
from Services import BirthdayService
from Generators import SimpleMessageGenerator, SimpleMessageWithFullNameGenerator, ElderPictureMessageGenerator, TailerMadeMessageGenerator
from datetime import date, datetime

app = Flask(__name__)

@app.route('/greetings/v1', methods=['POST'])
def greetings():
    output_type = request.args.get('format', default='JSON')
    db_type = request.args.get('db', default='memory')
    date_str = request.args.get('date', default=date.today())
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    generator = SimpleMessageGenerator()
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greetings = service.send_greetings(date_obj,output_type)
    greetings_string = '\n'.join(greetings)
    return greetings_string

@app.route('/greetings/v2', methods=['POST'])
def greetings_v2():
    output_type = request.args.get('format', default='JSON')
    db_type = request.args.get('db', default='memory')
    date_str = request.args.get('date', default=date.today())
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    generator = SimpleMessageWithFullNameGenerator()
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greetings = service.send_greetings(date_obj,output_type)
    greetings_string = '\n'.join(greetings)
    return greetings_string

@app.route('/greetings/v3', methods=['POST'])
def greetings_v3():
    output_type = request.args.get('format', default='JSON')
    db_type = request.args.get('db', default='memory')
    date_str = request.args.get('date', default=date.today())
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    picture_path = request.args.get('picture_path', default='')

    generator = ElderPictureMessageGenerator(picture_path)
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greetings = service.send_greetings(date_obj,output_type)
    greetings_string = '\n'.join(greetings)
    return greetings_string

@app.route('/greetings/v4', methods=['POST'])
def greetings_v4():
    output_type = request.args.get('format', default='JSON')

    db_type = request.args.get('db', default='memory')

    date_str = request.args.get('date', default=date.today())
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    discount_for_male: int = request.args.get('discount_for_male', default=0)
    items_for_male: list= request.args.getlist('items_for_male')
    discount_for_female: int = request.args.get('discount_for_female', default=0)
    items_for_female:list = request.args.getlist('items_for_female')

    generator = TailerMadeMessageGenerator(discount_for_male, items_for_male, discount_for_female, items_for_female)
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greetings = service.send_greetings(date_obj,output_type)
    greetings_string = '\n'.join(greetings)
    return greetings_string


def get_repo(db_type):
    if db_type == 'memory':
        from Repositories import MemoryMemberRepository
        return MemoryMemberRepository()
    elif db_type == 'mysql':
        from Repositories import MySQLMemberRepository
        return MySQLMemberRepository()
    elif db_type == 'mongo':
        from Repositories import MongoDBMemberRepository
        return MongoDBMemberRepository()
    else:
        raise ValueError(f'Unsupported db type: {db_type}')
    
