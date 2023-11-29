import pytest
from pages.api_reg_email import RegEmail
from selenium.webdriver.common.by import By
from pages.settings import *
import time
from pages.rostelecom import PageRecoveryPassword
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 9
@pytest.mark.recovery_pass
@pytest.mark.positive
def test_recovery_password(web_browser):
    """Проверка восстановления пароля при заполнении валидными данными.
    В начале теста требуется ОДНОРАЗОВЫЙ РУЧНОЙ ВВОД КАПЧИ !!!"""

    # Разделяем email на имя и домен для использования в следующих запросах:
    sign_at = valid_email.find('@')
    mail_name = valid_email[0:sign_at]
    mail_domain = valid_email[sign_at + 1:len(valid_email)]

    page = PageRecoveryPassword(web_browser)

    web_browser.implicitly_wait(10)

    page.email.send_keys(valid_email)

    time.sleep(20)           # ВРЕМЯ ДЛЯ ВВОДА КАПЧИ ВРУЧНУЮ

    page.btn_continue.click()

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
    web_browser.implicitly_wait(10)

    new_pass = fake_password
    page.new_password.send_keys(new_pass)
    web_browser.implicitly_wait(10)
    page.new_password_confirm.send_keys(new_pass)
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//button[@id="t-btn-reset-pass"]')))
    page.btn_reset_pass.click()
    time.sleep(30)

    # Проверка, что нас перенаправили на страницу авторизации для входа в свой кабинет с новым паролем.
    assert page.authorisation.is_presented()
    assert page.authorisation.get_text() == 'Авторизация'
