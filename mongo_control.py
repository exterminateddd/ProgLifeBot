from pymongo import MongoClient
from discord.member import Member

client = MongoClient("mongodb+srv://main_exterminated:secret_key@cluster0.tj4ux.gcp.mongodb.net/ProgLife?retryWrites=true&w=majority")
users = client['ProgLife']['users']


def db_command(func) -> bool:
    def wrap(*args):
        try:
            func(*args)
            return True
        except Exception as e:
            print(e)
            return False
    return wrap


@db_command
def add_user(data: Member) -> bool:
    users.insert_one({
        'id': data.id,
        'display_name': data.display_name,
        'proRoles': []
    })


def get_user_data(uid: int) -> bool:
    try:
        data = users.find_one({'id': uid})
        if not data: raise KeyError('')
        return data
    except: 
        return False


@db_command
def add_pro_role(uid: int, lang: str) -> bool:
    users.update({'id': uid}, {'$push': {'proRoles': lang}})


@db_command
def remove_pro_role(uid: int, lang: str) -> bool:
    users.update({'id': uid}, {'$pull': {'proRoles': lang}})


def user_has_role(uid: int, lang: str) -> bool:
    try:
        data = users.find_one({'id': uid})
        if not data: raise KeyError('')
        return lang in data['proRoles']
    except:
        print('exc')
        return False


def get_all_users():
    return [u for u in users.find({})]


def set_user_field(uid, k, v):
    users.update({'id': uid}, {'$set': {k: v}})
