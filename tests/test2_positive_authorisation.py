import time
import pytest
from pages.settings import *
from pages.api_reg_email import RegEmail
from pages.rostelecom import PageAuthorisation
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestPositivePageAuthorisation:
    """ Позитивные тесты страницы авторизации сайта https://lk.rt.ru/ """

    # 3
    @pytest.mark.auth
    @pytest.mark.positive
    def test_auth_tabs(self, web_browser):
        """Проверка вкладок на переключение и ввод данных,
         а также наличия и кликабельности всех необходимых элементов на странице."""

        page = PageAuthorisation(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

        page.tab_phone.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(valid_phone)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))

        page.tab_email.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(valid_email)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))

        page.tab_login.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(valid_login)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))

        page.tab_ls.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(valid_ls)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-eye-icon')))

        page.eye_password.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-checkbox__check-icon')))

        page.check_box.click()

        web_browser.implicitly_wait(10)

        assert page.tab_phone.is_presented() and page.tab_phone.is_clickable()
        assert page.tab_email.is_presented() and page.tab_email.is_clickable()
        assert page.tab_login.is_presented() and page.tab_login.is_clickable()
        assert page.tab_ls.is_presented() and page.tab_ls.is_clickable()
        assert page.username.is_presented()
        assert page.password.is_presented()
        assert page.eye_password.is_presented() and page.eye_password.is_clickable()
        assert page.check_box.is_presented() and page.check_box.is_clickable()
        assert page.link_forgot_pass.is_presented() and page.link_forgot_pass.is_clickable()
        assert page.btn_submit.is_presented() and page.btn_submit.is_clickable()
        assert page.btn_enter_temp_pass.is_presented() and page.btn_enter_temp_pass.is_clickable()
        assert page.link_auth_agr.is_presented() and page.link_auth_agr.is_clickable()
        assert page.btn_vk.is_presented() and page.btn_vk.is_clickable()
        assert page.btn_ok.is_presented() and page.btn_ok.is_clickable()
        assert page.btn_mail.is_presented() and page.btn_mail.is_clickable()
        assert page.btn_ya.is_presented() and page.btn_ya.is_clickable()
        assert page.link_reg.is_presented() and page.link_reg.is_clickable()
        assert page.link_faq.is_presented() and page.link_faq.is_clickable()
        assert page.phone_support.is_presented() and page.phone_support.is_clickable()

    # 4, 5, 6
    @pytest.mark.auth
    @pytest.mark.positive
    @pytest.mark.parametrize('username', [valid_phone, valid_login, valid_ls],
                             ids=['valid phone', 'valid_login', 'valid_ls'])
    def test_auth_valid_phone_login_ls_password(self, web_browser, username):
        """Проверка авторизации пользователя с валидными телефоном, почтой, логином, лицевым счётом и паролем."""

        page = PageAuthorisation(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(username)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))

        page.btn_submit.click()

        time.sleep(20)

        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'

    # 7
    @pytest.mark.auth
    @pytest.mark.positive
    def test_auth_valid_email_password(self, web_browser):
        """Проверка авторизации пользователя с валидными почтой и паролем.
        Требуется ввод капчи вручную, т.к. срабатывает защита сайта."""

        page = PageAuthorisation(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        web_browser.implicitly_wait(10)

        page.username.send_keys(valid_email)

        web_browser.implicitly_wait(10)

        page.password.send_keys(valid_pass_reg)

        time.sleep(30)                # ВРЕМЯ ДЛЯ ВВОДА КАПЧИ ВРУЧНУЮ

        page.btn_submit.click()

        time.sleep(20)

        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'

    # 8
    @pytest.mark.auth
    @pytest.mark.positive
    def test_auth_temp_code(self, web_browser):
        """Проверка авторизации пользователя по временному коду.
        Требуется ввод капчи вручную, т.к. срабатывает защита сайта."""

        # Разделяем email на имя и домен для использования в следующих запросах:
        sign_at = valid_email.find('@')
        mail_name = valid_email[0:sign_at]
        mail_domain = valid_email[sign_at + 1:len(valid_email)]

        page = PageAuthorisation(web_browser)

        web_browser.implicitly_wait(10)

        page.inp_address.send_keys(valid_email)

        time.sleep(30)                 # ВРЕМЯ ДЛЯ ВВОДА КАПЧИ

        page.btn_get_code.click()

        time.sleep(15)

        """Проверяем почтовый ящик на наличие писем и достаём ID последнего письма"""
        result_id, status_id = RegEmail().get_id_letter(mail_name, mail_domain)
        # Получаем id письма с кодом из почтового ящика:
        id_letter = result_id[0].get('id')
        # Сверяем полученные данные с нашими ожиданиями
        assert status_id == 200, "status_id error"
        assert id_letter > 0, "id_letter > 0 error"

        """Получаем код регистрации из письма от Ростелекома"""
        result_code, status_code = RegEmail().get_reg_code(mail_name, mail_domain, str(id_letter))

        # Получаем body из текста письма:
        text_body = result_code.get('body')
        # Извлекаем код из текста методом find:
        reg_code = text_body[text_body.find('Ваш код: ') + len('Ваш код: '):
                             text_body.find('Ваш код: ') + len('Ваш код: ') + 6]
        # Сверяем полученные данные с нашими ожиданиями
        assert status_code == 200, "status_code error"
        assert reg_code != '', "reg_code != [] error"

        reg_digit = [int(char) for char in reg_code]
        print(reg_digit)
        web_browser.implicitly_wait(30)
        for i in range(0, 6):
            web_browser.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[i].send_keys(reg_code[i])
            web_browser.implicitly_wait(5)

        time.sleep(15)

        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
