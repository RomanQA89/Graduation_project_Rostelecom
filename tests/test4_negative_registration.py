import pytest
from pages.rostelecom import PageRegistration
from pages.settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestNegativePageRegistration:
    """ Негативные тесты страницы регистрации сайта https://lk.rt.ru/ """

    # 10, 11, 12, 13, 14, 15, 16, 17, 18
    @pytest.mark.registration
    @pytest.mark.negative
    @pytest.mark.parametrize('firstname', ['', special_chars(), generate_string_rus(1), generate_string_rus(31),
                                           generate_string_rus(256), generate_string_rus(1000),
                                           invalid_username_2, english_chars(), chinese_chars()],
                             ids=['empty', 'special_chars', '1_rus_chars', '31_rus_chars', '256_rus_chars',
                                  '1000_rus_chars', 'number', 'eng_chars', 'chinese_chars'])
    def test_registration_invalid_firstname(self, web_browser, firstname):
        """Проверка регистрации пользователей с невалидными именами. Негативные тесты."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        page.name.send_keys(firstname)

        web_browser.implicitly_wait(10)

        page.last_name.send_keys(fake_lastname)

        web_browser.implicitly_wait(10)

        page.select_town.click()

        web_browser.implicitly_wait(10)

        page.my_town.click()

        web_browser.implicitly_wait(10)

        page.email_and_mobile.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_pass_reg)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(valid_pass_reg)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        web_browser.implicitly_wait(10)

        assert page.note_text_error.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    # 19, 20, 21, 22, 23, 24, 25, 26, 27
    @pytest.mark.registration
    @pytest.mark.negative
    @pytest.mark.parametrize('lastname', ['', special_chars(), generate_string_rus(1), generate_string_rus(31),
                                          generate_string_rus(256), generate_string_rus(1000),
                                          invalid_username_2, english_chars(), chinese_chars()],
                             ids=['empty', 'special_chars', '1_rus_chars', '31_rus_chars', '256_rus_chars',
                                  '1000_rus_chars', 'number', 'eng_chars', 'chinese_chars'])
    def test_registration_invalid_lastname(self, web_browser, lastname):
        """Проверка регистрации пользователей с невалидными фамилиями. Негативные тесты."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        page.name.send_keys(fake_firstname)

        web_browser.implicitly_wait(10)

        page.last_name.send_keys(lastname)

        web_browser.implicitly_wait(10)

        page.select_town.click()

        web_browser.implicitly_wait(10)

        page.my_town.click()

        web_browser.implicitly_wait(10)

        page.email_and_mobile.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_pass_reg)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(valid_pass_reg)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        web_browser.implicitly_wait(10)

        assert page.note_text_error.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    # 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38
    @pytest.mark.registration
    @pytest.mark.negative
    @pytest.mark.parametrize('email', [invalid_mail_1, invalid_mail_2, invalid_mail_3, invalid_mail_4,
                                       invalid_mail_5, invalid_mail_6, invalid_mail_7, invalid_mail_8,
                                       invalid_mail_9, f'{russian_chars()}@mail.ru', f'{chinese_chars()}@mail.ru'],
                             ids=['empty', 'invalid_email_2', 'invalid_email_3', 'invalid_email_4', 'invalid_email_5',
                                  'invalid_email_6', 'invalid_email_7', 'invalid_email_8', 'invalid_email_9',
                                  'russian_chars', 'chinese_chars'])
    def test_registration_invalid_email(self, web_browser, email):
        """Проверка регистрации пользователей с невалидными почтами. Негативные тесты."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        page.name.send_keys(fake_firstname)

        web_browser.implicitly_wait(10)

        page.last_name.send_keys(fake_lastname)

        web_browser.implicitly_wait(10)

        page.select_town.click()

        web_browser.implicitly_wait(10)

        page.my_town.click()

        web_browser.implicitly_wait(10)

        page.email_and_mobile.send_keys(email)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_pass_reg)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(valid_pass_reg)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        web_browser.implicitly_wait(10)

        assert page.note_text_error.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                  'или email в формате example@email.ru'

    # 39, 40, 41
    @pytest.mark.registration
    @pytest.mark.negative
    @pytest.mark.parametrize('phone', [invalid_username_2, invalid_username_5, invalid_username_6],
                             ids=['1_number', '12_number', '10_number'])
    def test_registration_invalid_phone(self, web_browser, phone):
        """Проверка регистрации пользователей с невалидными телефонами. Негативные тесты."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        page.name.send_keys(fake_firstname)

        web_browser.implicitly_wait(10)

        page.last_name.send_keys(fake_lastname)

        web_browser.implicitly_wait(10)

        page.select_town.click()

        web_browser.implicitly_wait(10)

        page.my_town.click()

        web_browser.implicitly_wait(10)

        page.email_and_mobile.send_keys(phone)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_pass_reg)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(valid_pass_reg)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        web_browser.implicitly_wait(10)

        assert page.note_text_error.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                  'или email в формате example@email.ru'

    # 42, 43, 44, 45, 46, 47, 48, 49, 50, 51
    @pytest.mark.registration
    @pytest.mark.negative
    @pytest.mark.parametrize('password', ['', special_chars(), generate_string_en(1), generate_string_en(7),
                                          generate_string_en(9), generate_string_en(19), generate_string_en(21),
                                          generate_string_rus(10), chinese_chars(), 'STATEMENT156'],
                             ids=['empty', 'special_chars', '1_en_chars', '7_en_chars', '9_en_chars',
                                  '19_en_chars', '21_en_chars', 'rus_chars', 'chinese_chars', 'upper_letters'])
    def test_registration_invalid_password(self, web_browser, password):
        """Проверка регистрации пользователей с невалидными паролями. Негативные тесты."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        page.name.send_keys(fake_firstname)

        web_browser.implicitly_wait(10)

        page.last_name.send_keys(fake_lastname)

        web_browser.implicitly_wait(10)

        page.select_town.click()

        web_browser.implicitly_wait(10)

        page.my_town.click()

        web_browser.implicitly_wait(10)

        page.email_and_mobile.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.password.send_keys(password)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        web_browser.implicitly_wait(10)

        assert page.note_text_error.get_text() == 'Длина пароля должна быть не менее 8 символов' \
               or 'Пароль должен содержать хотя бы одну заглавную букву' or \
               'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or \
               'Длина пароля должна быть не более 20 символов' or 'Пароль должен содержать только латинские буквы' or \
               'Пароль должен содержать хотя бы одну строчную букву'

    # 52, 53
    @pytest.mark.registration
    @pytest.mark.negative
    @pytest.mark.parametrize('email_and_phone', [valid_email, valid_phone],
                             ids=['email_is_already_exists', 'phone_is_already_exists'])
    def test_registration_account_already_exists(self, web_browser, email_and_phone):
        """Проверка повторной регистрации пользователя по уже зарегистрированному на сайте номеру телефона и почте.
        Негативные тесты."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        page.name.send_keys(fake_firstname)

        web_browser.implicitly_wait(10)

        page.last_name.send_keys(fake_lastname)

        web_browser.implicitly_wait(10)

        page.select_town.click()

        web_browser.implicitly_wait(10)

        page.my_town.click()

        web_browser.implicitly_wait(10)

        page.email_and_mobile.send_keys(email_and_phone)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(valid_password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        web_browser.implicitly_wait(10)

        assert page.account_is_exist.get_text() == 'Учётная запись уже существует'

    # 54
    @pytest.mark.registration
    @pytest.mark.negative
    def test_registration_passwords_dont_match(self, web_browser):
        """Проверка на совпадение паролей.
        Негативные тесты."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        page.name.send_keys(fake_firstname)

        web_browser.implicitly_wait(10)

        page.last_name.send_keys(fake_lastname)

        web_browser.implicitly_wait(10)

        page.select_town.click()

        web_browser.implicitly_wait(10)

        page.my_town.click()

        web_browser.implicitly_wait(10)

        page.email_and_mobile.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(valid_pass_reg)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        web_browser.implicitly_wait(10)

        assert page.note_text_error.get_text() == 'Пароли не совпадают'
