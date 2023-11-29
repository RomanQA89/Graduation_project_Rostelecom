import time
import pytest
from pages.rostelecom import PageAuthorisation
from pages.settings import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestNegativePageAuthorisation:
    """ Позитивные тесты страницы авторизации сайта https://lk.rt.ru/ """

    @pytest.mark.auth
    @pytest.mark.negative
    @pytest.mark.parametrize('email', [invalid_mail_1, invalid_mail_2, invalid_mail_3, invalid_mail_4,
                                       invalid_mail_5, invalid_mail_6, invalid_mail_7],
                             ids=['empty', 'empty_mail_name', 'empty_domain_name', 'special_chars',
                                  'no_point', 'no_domain', 'number_domain'])
    def test_auth_temp_code_invalid_email(self, web_browser, email):
        """Проверка авторизации по временному коду с невалидными почтами. Негативные тесты."""

        page = PageAuthorisation(web_browser)

        web_browser.implicitly_wait(10)

        page.inp_address.send_keys(email)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'otp_get_code')))

        page.btn_get_code.click()

        web_browser.implicitly_wait(10)

        assert page.error_mail.is_presented()
        assert page.error_mail.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX,' \
                                             ' или email в формате example@email.ru'

    @pytest.mark.auth
    @pytest.mark.negative
    @pytest.mark.parametrize('phone', [invalid_username_1, invalid_username_2, invalid_username_3],
                             ids=['empty_phone', 'one_number', 'nine_numbers'])
    def test_auth_invalid_phone(self, web_browser, phone):
        """Проверка авторизации по невалидным номерам телефонов. Негативные тесты."""

        page = PageAuthorisation(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(phone)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))

        page.btn_submit.click()

        web_browser.implicitly_wait(10)

        assert page.error_mail.is_presented() and page.error_mail.get_text() == 'Введите номер телефона'\
               or 'Неверный формат телефона'

    @pytest.mark.auth
    @pytest.mark.negative
    def test_auth_empty_email(self, web_browser):
        """Проверка авторизации по не введенной почте. Негативный тест."""

        page = PageAuthorisation(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))

        page.tab_email.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(invalid_mail_1)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))

        page.btn_submit.click()

        web_browser.implicitly_wait(10)

        assert page.error_mail.is_presented() and page.error_mail.get_text() == 'Введите адрес, указанный при регистрации'

    @pytest.mark.auth
    @pytest.mark.negative
    @pytest.mark.parametrize('login', [invalid_username_1, invalid_username_2, generate_string_en(5), special_chars(),
                                       generate_string_en(256), generate_string_en(1000), russian_chars()],
                             ids=['empty', 'number', 'eng_chars', 'special_chars', '256_eng_chars', '1000_eng_chars',
                                  'rus_chars'])
    def test_auth_invalid_login(self, web_browser, login):
        """Проверка авторизации по невалидным логинам. Негативный тест.
        Требуется ввод капчи вручную, т.к. срабатывает защита сайта."""

        page = PageAuthorisation(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))

        page.tab_login.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(login)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        time.sleep(20)                       # ВРЕМЯ ДЛЯ ВВОДА КАПЧИ ВРУЧНУЮ

        page.btn_submit.click()

        web_browser.implicitly_wait(10)

        assert page.error_message.get_text() == 'Неверный логин или пароль'\
               or page.error_mail.get_text() == 'Введите логин, указанный при регистрации'

    @pytest.mark.auth
    @pytest.mark.negative
    @pytest.mark.parametrize('ls', [invalid_username_1, invalid_username_2, invalid_username_4, invalid_username_5],
                             ids=['empty_ls', 'one_number', '11_numbers', '12_numbers'])
    def test_auth_invalid_ls(self, web_browser, ls):
        """Проверка авторизации по невалидным лицевым счетам. Негативный тест."""

        page = PageAuthorisation(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))

        page.tab_ls.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(ls)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))

        page.btn_submit.click()

        web_browser.implicitly_wait(10)

        assert page.error_message.get_text() == 'Неверный логин или пароль' \
               or page.error_mail.get_text() == 'Введите номер вашего лицевого счета'\
               or 'Проверьте, пожалуйста, номер лицевого счета'
