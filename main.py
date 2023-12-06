from flask import Flask, jsonify, request
from Services import BirthdayService
from Generators import SimpleMessageGenerator, SimpleMessageWithFullNameGenerator, ElderPictureMessageGenerator, TailerMadeMessageGenerator
app = Flask(__name__)

@app.route('/greetings/v1', methods=['POST'])
def greetings():
    output_type = request.args.get('format', default='JSON')
    db_type = request.args.get('db', default='memory')
    generator = SimpleMessageGenerator()
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greeting = service.send_greetings(output_type)
    return greeting

@app.route('/greetings/v2', methods=['POST'])
def greetings_v2():
    output_type = request.args.get('format', default='JSON')
    db_type = request.args.get('db', default='memory')
    generator = SimpleMessageWithFullNameGenerator()
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greeting = service.send_greetings(output_type)
    return greeting

@app.route('/greetings/v3', methods=['POST'])
def greetings_v3():
    output_type = request.args.get('format', default='JSON')
    db_type = request.args.get('db', default='memory')
    generator = ElderPictureMessageGenerator()
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greeting = service.send_greetings(output_type)
    return greeting

@app.route('/greetings/v4', methods=['POST'])
def greetings_v4():
    output_type = request.args.get('format', default='JSON')
    db_type = request.args.get('db', default='memory')
    generator = TailerMadeMessageGenerator()
    repo = get_repo(db_type)
    service = BirthdayService(repo, generator)
    greeting = service.send_greetings(output_type)
    return greeting


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
    
