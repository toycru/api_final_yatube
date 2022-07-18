# Yatube API
API для взаимодействия с блогами Yatube.

## Содержание
- [Технологии](#технологии)
- [Deploy](#deploy)
- [Использование](#использование)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- Django 2.2.16
- djangorestframework 3.12.4
- djangorestframework-simplejwt 4.7.2
- Pillow 8.3.1
- PyJWT 2.1.0

## Deploy
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

## Использование
 Yatube API принимает POST, GET, PUT, PATCH и DELETE-запросы в зависимости от выполняемого действия. Тип и адрес запроса для требуемого действия можно найти в [документации](http://127.0.0.1:8000/redoc/) после установки.
 Текст самого запроса должен соответствовать формату JSON.

 Для запросов доступны следующие эдпоинты:
 - /api/v1/posts/
 - /api/v1/posts/{id}/
 - /api/v1/posts/{post_id}/comments/
 - /api/v1/posts/{post_id}/comments/{id}/
 - /api/v1/groups/
 - /api/v1/groups/{id}/
 - /api/v1/follow/
 - /api/v1/jwt/create/
 - /api/v1/jwt/refresh/

### Пример GET-запроса к эндпоинту /api/v1/posts/
Адрес запроса:
```typescript
http://127.0.0.1:8000/api/v1/posts/
```
Ответ:
```typescript
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Пример POST-запроса к эндпоинту /api/v1/posts/
Адрес запроса:
```typescript
http://127.0.0.1:8000/api/v1/posts/
```
Запрос:
```typescript
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Ответ:
```typescript
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

## To do
- [x] Добавить крутое README
- [ ] Закрыть спринт

## Команда проекта

- [Dmitry ToyCru](https://toycru.ru/) — Back-End Engineer