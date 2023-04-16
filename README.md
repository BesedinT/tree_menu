# tree_menu

## Краткое описание

Django-приложение, которое реализует древовидное меню.

## Технологии  

Python 3.7  
Django 3.2  

### Установка и настройка
Склонируйте репозиторий:
```
git clone git@github.com:BesedinT/tree_menu.git
```
Установите зависимости:
```
pip install -r requirements.txt
```
Создайте миграции и примените их:
```
python manage.py makemigrations
python manage.py migrate
```
Создайте суперпользователя:
```
python manage.py createsuperuser
```
Запустите сервер:
```
python manage.py runserver
```

Перейдите на [страницу администрирования](http://127.0.0.1:8000/admin/) введите логин и пароль, созданные на предыдущем шаге.
Добавьте меню через административную панель.
