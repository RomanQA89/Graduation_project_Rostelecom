import time
import pytest
from pages.rostelecom import PageRegistration
from pages.api_reg_email import RegEmail
from pages.settings import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestPositivePageRegistration:
    """ Позитивные тесты страницы регистрации сайта https://lk.rt.ru/ """
# 1
    @pytest.mark.registration
    @pytest.mark.positive
    def test_page_registration_check(self, web_browser):
        """Проверка перехода на страницу регистрации и наличия полей для заполнения данными."""

        page = PageRegistration(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))

        page.btn_enter.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.ID, 'kc-register')))

        page.link_enter.click()

        web_browser.implicitly_wait(10)

        assert page.email_and_mobile.is_presented()
        assert page.name.is_presented()
        assert page.last_name.is_presented()
        assert page.select_town.is_presented()
        assert page.password.is_presented()
        assert page.pass_confirm.is_presented()
        assert page.btn_register.is_presented()
        assert page.rt_link.is_presented()
        assert page.logo_and_tagline.is_presented()

    # Выносим данные в тело класса для доступа к значениям переменных из всех функций класса:
    result_email, status_email = RegEmail().get_api_email()       # запрос на получение валидного почтового ящика
    email_reg = result_email[0]                                   # из запроса получаем валидный email

    # 2
    @pytest.mark.registration
    @pytest.mark.positive
    def test_valid_name_lastname(self, web_browser):
        """Проверка регистрации нового пользователя при заполнении валидными данными.
        Используем виртуальный почтовый ящик '1secmail.com' и получаем данные через GET запросы.
        Добавляем созданный email в файл settings."""

        # Разделяем email на имя и домен для использования в следующих запросах:
        sign_at = self.email_reg.find('@')
        mail_name = self.email_reg[0:sign_at]
        mail_domain = self.email_reg[sign_at + 1:len(self.email_reg)]
        assert self.status_email == 200, 'status_email error'
        assert len(self.result_email) > 0, 'len(result_email) > 0 -> error'

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

        page.email_and_mobile.send_keys(self.email_reg)

        web_browser.implicitly_wait(10)

        page.password.send_keys(fake_password)

        web_browser.implicitly_wait(10)

        page.pass_confirm.send_keys(fake_password)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.NAME, 'register')))

        page.btn_register.click()

        time.sleep(30)

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
        reg_code = text_body[text_body.find('Ваш код : ') + len('Ваш код : '):
                             text_body.find('Ваш код : ') + len('Ваш код : ') + 6]
        # Сверяем полученные данные с нашими ожиданиями
        assert status_code == 200, "status_code error"
        assert reg_code != '', "reg_code != [] error"

        reg_digit = [int(char) for char in reg_code]
        web_browser.implicitly_wait(30)
        for i in range(0, 6):
            web_browser.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[i].send_keys(reg_code[i])
            web_browser.implicitly_wait(5)

        time.sleep(20)

        page.btn_enter_my_page.click()

        time.sleep(20)   # Ждём когда страница личного кабинета пользователя полностью загрузится.

        """Проверяем, что регистрация пройдена и пользователь перенаправлен в личный кабинет"""
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main', 'Регистрация НЕ пройдена'
        page._web_driver.save_screenshot('Reg_success.png')

        """В случае успешной регистрации, перезаписываем созданные пару email/пароль в файл settings"""
        page._web_driver.save_screenshot('Reg_success.png')
        print(self.email_reg, fake_password)
        with open(r"C:\Users\Пользователь\PycharmProjects\Graduation_project_Rostelecom\pages\settings.py", 'r', encoding='utf8') as file:
            lines = []
            print(lines)
            for line in file.readlines():
                if 'valid_email' in line:
                    lines.append(f"valid_email = '{str(self.email_reg)}'\n")
                elif 'valid_pass_reg' in line:
                    lines.append(f"valid_pass_reg = '{fake_password}'\n")
                else:
                    lines.append(line)
        with open(r"C:\Users\Пользователь\PycharmProjects\Graduation_project_Rostelecom\pages\settings.py", 'w', encoding='utf8') as file:
            file.writelines(lines)
