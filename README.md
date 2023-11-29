Итоговый проект по автоматизации тестирования функционала страницы https://lk.rt.ru/ сайта "Ростелеком"

При тестировании сайта были написаны:

- тест-кейсы;

- баг-репорты;

- автоматизированные тесты.

При тестировании сайта были применены следующие техники тест-дизайна:

- разбиение на классы эквивалентности;
- анализ граничных значений.

Данные техники применялись для полей ввода данных при тестировании негативных сценариев.

Некоторые автотесты требуют ручной ввод капчи с картинки, т.к. срабатывает защита сайта.

Папка pages содержит следующие файлы:

api_reg_email.py - GET-запросы к виртуальному почтовому ящику (1secmail.com) для получения валидного email и кода для регистрации на сайте и восстановления пароля;
elements.py - функции для взаимодействия с элементами страницы сайта при проведении автотестов;
base.py - функции для получения главной страницы сайта и пути текущей страницы;
rostelecom.py - функции для взаимодействия с url страницами и локаторы для элементов сайта;
settings.py - учетные данные, используемые в процессе теста.
Папка tests содержит следующие файлы:
test1_positive_registration.py - позитивные тесты страницы регистрации;
test2_positive_authorisation.py - позитивные тесты страницы авторизации;
test3_positive_recovery_pass.py - позитивные тесты страницы восстановления пароля;
test4_negative_registration.py - негативные тесты страницы регистрации;
test5_negative_authorisation.py - негативные тесты страницы авторизации;
test6_negative_recovery_pass.py - негативные тесты страницы восстановления пароля.
Также проект содержит такие файлы, как:
conftest.py - фикстуры для работы с браузером;
pytest.ini - маркеры для параметризации;
requirements.txt - используемые при тестировании библиотеки PyCharm.
Для подготовки к запуску автотестов необходимо установить необходимые библиотеки PyCharm с помощью вводимой команды в консоли терминала:


pip install -r requirements.txt


Также необходимо ввести валидные данные уже авторизованного пользователя на сайте в файле .env и скачать актуальную версию драйвера для вашего браузера для успешного прохождения автотестов.


Для запуска автотестов необходимо вводить команды в консоли терминала.


Для позитивных тестов страницы регистрации:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test1_positive_registration.py -k TestPositivePageRegistration


Для позитивных тестов страницы авторизации:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test2_positive_authorisation.py -k TestPositivePageAuthorisation

Для позитивных тестов страницы восстановления пароля:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test3_positive_recovery_pass.py


Для негативных тестов страницы регистрации:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test4_negative_registration.py -k TestNegativePageRegistration


Для негативных тестов страницы авторизации:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test5_negative_authorisation.py -k TestNegativePageAuthorisation


Для негативных тестов страницы восстановления пароля:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test6_negative_recovery_pass.py -k TestNegativePageRecoveryPass


<chromedriver_directory>\<chromedriver_file> - путь к директории файла драйвера\название файла браузера. Например: C:\Chrome-selenium\chromedriver.exe
