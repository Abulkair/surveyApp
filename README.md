Склонируйте репозиторий с помощью git

    https://github.com/Abulkair/surveyApp.git
Перейти в папку:
```bash
cd surveyApp
```
Создать и активировать виртуальное окружение env.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:

```bash
Username (leave blank to use 'admin'): admin
Email address: user@user.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/


* _Документация API_ (http://127.0.0.1:8000/swagger/ )
