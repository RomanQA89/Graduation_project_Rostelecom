from pages.base import WebPage
from pages.elements import WebElement


class PageRegistration(WebPage):
    """Локаторы для страницы регистрации."""

    def __init__(self, web_driver, url=''):
        url = 'https://lk.rt.ru/'
        super().__init__(web_driver, url)

    # Кнопка "Войти с паролем"
    btn_enter = WebElement(id='standard_auth_btn')

    # Ссылка "Зарегистрироваться"
    link_enter = WebElement(id='kc-register')

    # Поле ввода электронной почты или телефона
    email_and_mobile = WebElement(id='address')

    # Поле ввода "Имя"
    name = WebElement(name='firstName')

    # Поле ввода "Фамилия"
    last_name = WebElement(name='lastName')

    # Поле ввода региона проживания
    select_town = WebElement(class_name='rt-select__input')

    # Поле ввода "Пароль"
    password = WebElement(id='password')

    # Поле ввода "Подтверждение пароля"
    pass_confirm = WebElement(id='password-confirm')

    # Кнопка "Зарегистрироваться"
    btn_register = WebElement(name='register')

    # Ссылка на пользовательское соглашение
    rt_link = WebElement(id='rt-auth-agreement-link')

    # Логотип и слоган сайта
    logo_and_tagline = WebElement(class_name='what-is-container__logo-container' and 'what-is__desc')

    # Сообщение о неверно введенных имени и фамилии
    note_text_error = WebElement(class_name='rt-input-container__meta--error')

    # Выбор своего региона из выпадающего списка
    my_town = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[18]')

    # Кнопка "Войти в кабинет"
    btn_enter_my_page = WebElement(class_name='n-button')

    # Уведомление о существовании учётной записи
    account_is_exist = WebElement(class_name='card-modal__title')


class PageRecoveryPassword(WebPage):
    """Локаторы для страницы восстановления пароля."""

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=lk_b2c&tab_id=cKYVYTAESnM'
        super().__init__(web_driver, url)

    # Поле ввода электронной почты
    email = WebElement(id='username')

    # Поле для ввода капчи
    captcha = WebElement(id='captcha')

    # Кнопка "Продолжить"
    btn_continue = WebElement(id='reset')

    # Шестизначный код для восстановления пароля
    six_digit_code = WebElement(xpath='//input[@inputmode="numeric"]')

    # Поле ввода "Новый пароль"
    new_password = WebElement(id='password-new')

    # Поле ввода "Подтверждение нового пароля"
    new_password_confirm = WebElement(id='password-confirm')

    # Кнопка "Сохранить"
    btn_reset_pass = WebElement(xpath='//button[@id="t-btn-reset-pass"]')

    # Обозначение страницы авторизации
    authorisation = WebElement(class_name='card-container__title')


class PageAuthorisation(WebPage):
    """Локаторы для страницы авторизации."""

    def __init__(self, web_driver, url=''):
        url = 'https://lk.rt.ru/'
        super().__init__(web_driver, url)

    # Кнопка "Войти с паролем"
    btn_enter = WebElement(id='standard_auth_btn')

    # Вкладка "Телефон"
    tab_phone = WebElement(id='t-btn-tab-phone')

    # Вкладка "Почта"
    tab_email = WebElement(id='t-btn-tab-mail')

    # Вкладка "Логин"
    tab_login = WebElement(id='t-btn-tab-login')

    # Вкладка "Лицевой счёт"
    tab_ls = WebElement(id='t-btn-tab-ls')

    # Поле для ввода телефона, почты, логина и лицевого счета
    username = WebElement(id='username')

    # Поле для ввода пароля
    password = WebElement(id='password')

    # Кнопка видимости пароля
    eye_password = WebElement(class_name='rt-eye-icon')

    # Радиобаттон "Запомнить меня"
    check_box = WebElement(class_name='rt-checkbox__shape')

    # Ссылка "Забыл пароль"
    link_forgot_pass = WebElement(id='forgot_password')

    # Кнопка "Войти"
    btn_submit = WebElement(id='kc-login')

    # Кнопка "Войти по временному коду"
    btn_enter_temp_pass = WebElement(id='back_to_otp_btn')

    # Ссылка на условия пользовательского соглашения
    link_auth_agr = WebElement(id='rt-auth-agreement-link')

    # Кнопка входа через Вконтакте
    btn_vk = WebElement(id='oidc_vk')

    # Кнопка входа через Одноклассники
    btn_ok = WebElement(id='oidc_ok')

    # Кнопка входа через Mail.ru
    btn_mail = WebElement(id='oidc_mail')

    # Кнопка входа через Яндекс
    btn_ya = WebElement(id='oidc_ya')

    # Ссылка на страницу регистрации
    link_reg = WebElement(id='kc-register')

    # Ссылка на раздел с ответами на вопросы
    link_faq = WebElement(class_name='faq-modal-tip__btn')

    # Ссылка на телефон службы поддержки
    phone_support = WebElement(class_name='rt-footer-right')

    # Кнопка "Получить код"
    btn_get_code = WebElement(id='otp_get_code')

    # Поле ввода почты
    inp_address = WebElement(id='address')

    # Отображение ошибки ввода под полем ввода почты
    error_mail = WebElement(class_name='rt-input-container__meta--error')

    # Сообщение об ошибке
    error_message = WebElement(id='form-error-message')
