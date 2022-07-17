# Yatube API
API для взаимодействия с блогами Yatube.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-ci/cd)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- Django 2.2.16
- djangorestframework 3.12.4
- djangorestframework-simplejwt 4.7.2
- Pillow 8.3.1
- PyJWT 2.1.0


## Использование
- Клонируйте репозиторий:
```typescript
 git clone https://github.com/toycru/api_final_yatube.git
```
- Разверните виртуальное окружение
```typescript 
python -m venv venv
```
- Установите зависимости
```typescript
pip install -r requirements.txt
```
- Выполните миграции
```typescript
python yatube_api/manage.py migrate 
```
- Запустите сервер
```typescript
python yatube_api/manage.py runserver
```

## FAQ 
- Как работать с вашим приложением?
- Почитайте [Документацию](http://127.0.0.1:8000/redoc/) 

## To do
- [x] Добавить крутое README
- [ ] Закрыть спринт

## Команда проекта

- [Dmitry ToyCru](https://toycru.ru/) — Back-End Engineer