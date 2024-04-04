# Сервис, позволяющий подгружать текстовый файл и определять у слов, входящих в состав документа, такие параметры как tf и idf.

## Запуск проекта
### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlexShemyakin/read_file_project.git
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

```
python -m pip install --upgrade pip
```

### Создать в директории проекта, где располагается файл settings.py, файл .env и записать в него секретный ключ (SECRET_KEY). 

```
<-- Файл .env -->

SECRET_KEY=huasbd7y71ehasbdf7y19cmsald9312uec
```

### Выполнить миграции, сбор статических файлов и запуск локального сервера:

```
backend python manage.py migrate
python manage.py runserver
```

Теперь локальный сервер доступен по адресу http://127.0.0.1/


## Автор проекта
[Шемякин Александр](https://github.com/AlexShemyakin)

## Стек технологий
Разработка:

[Django]
[Python]
[HTML]
