import os
from dotenv import load_dotenv
from faker import Faker
import string
load_dotenv()


"""Фейковые данные для авторизации в системе"""
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()
fake_password = fake.password()
fake_login = fake.user_name()
fake_email = fake.email()

"""Валидные данные для авторизации в системе"""
valid_phone = os.getenv('phone')
valid_login = os.getenv('login')
valid_password = os.getenv('password')
valid_ls = os.getenv('ls')

valid_email = 'xzpk9hk@txcct.com'
valid_pass_reg = 'w+U6ZWEw&K'

"""Невалидные данные для авторизации в системе.(Для негативных тестов.)"""
invalid_mail_1 = ''
invalid_mail_2 = '@'
invalid_mail_3 = '@.'
invalid_mail_4 = 'b2cb4a217it@'
invalid_mail_5 = '@laafd.com'
invalid_mail_6 = 'b2cb4a217it@laafd.'
invalid_mail_7 = 'b2cb4a217it@laafdcom'
invalid_mail_8 = 'b2cb4a217it@laafd.77'
invalid_mail_9 = '.'

invalid_username_1 = ''
invalid_username_2 = '6'
invalid_username_3 = '123456789'
invalid_username_4 = '87696976766'
invalid_username_5 = '896969767656'
invalid_username_6 = '8945345356'


def generate_string_rus(n):
    return 'б' * n


def generate_string_en(n):
    return 'x' * n


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def chinese_chars():    # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return f'{string.punctuation}'
