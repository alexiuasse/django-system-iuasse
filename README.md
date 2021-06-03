# Django System Iuasse

Django Iuasse System is a system that aims to run a small tech business, that make web services (like one page, web system, application mobile with backend and so on).

#### Few Considerations

1. My main language is not english, so i am 100% sure that has some language errors.
2. Some models name are not really well designed (but it works).
3. The default localization are only made from english to pt_BR.
4. There are always some improvement to be made.
5. Use this project to learn more about Django, i am not an expert but i put everything that i know in this project. (It's ain't much, but it's honest work.)

## Quick Tutorial

To run this project you need to do:

#### Atention

If you use **Windows** the package **mysql-client** might not get installed correctly, so you need to install it manually, just go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient and get the correct whl for your system. (To install just use ```pip install name_of_package.whl```.)

1. Install **python 3.8** (that is the version that i use, i think you can use other version to)
2. Make a virtual environment (what i do is ```virtualenv venv```)
3. Run ```pip install -r requirements.txt```(this will install all libs that it needs to run)
4. Open a terminal/cmd into app folder (where the manage.py is)
5. Run ```python manage.py runserver 0.0.0.0:8000```

If you wanna a fresh start run, after phase 4:

1. ```find . -path "*/migrations/*.py" -not -name "__init__.py" -delete```
2. ```find . -path "*/migrations/*.pyc"  -delete```
3. **Delete** the **db.sqlite3**
4. Run ```python manage.py makemigrations```
5. Run ```python manage.py migrate```
6. Run ```python manage.py createsuperuser```
7. Run ```python manage.py runserver 0.0.0.0:8000```

#### username: admin  password: admin123

## About Structure

For now the structure consists:

1. Client, a module that provides a way to manage a client.
2. Financial, a module for financial things, here you can make a financial release that can be a asset or liability (you must provide the proper cost center).
3. Service, a module that has the services provide by the company, the idea is that all services has a contract. The only service available now is a WebService that aims to create a web system, web page and so on.

## Localization

https://docs.djangoproject.com/en/3.2/topics/i18n/translation/

1. ```django-admin makemessages -l pt_BR```
2. ```django-admin compilemessages```

## License

This project is under MIT License.
