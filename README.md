Задание

Объедините студентов в команды по 2-5 человек в сессионных залах.

Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет"

"Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание.

Критерии оценивания:
1 - Слушатель создал базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.


# Результат и описание работы

Команда для запуска в консоли
> uvicorn main:app --reload

Вывод в консоли:
    
    INFO:     Application startup complete.

## filling_base

Наполняем базу данными: http://127.0.0.1:8000/filling_base/25

Ответ:
    
    {"message":"25 users, items and orders create"}

Вывод в консоли:

    INFO:     127.0.0.1:65523 - "GET /filling_base/25 HTTP/1.1" 200 O

### GET для вывода всех пользователей, товаров и заказов

* http://127.0.0.1:8000/users/
* http://127.0.0.1:8000/items/
* http://127.0.0.1:8000/orders/

Вывод в консоли:

    INFO:     127.0.0.1:49334 - "GET /users/ HTTP/1.1" 200 OK
    INFO:app:Отработал GET запрос.
    INFO:     127.0.0.1:49335 - "GET /items/ HTTP/1.1" 200 OK
    INFO:app:Отработал GET запрос.
    INFO:     127.0.0.1:49336 - "GET /orders/ HTTP/1.1" 200 OK

### POST для пользователя

Проверим добавление пользователя:

    curl -X 'POST' \
    'http://127.0.0.1:8000/users/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "user_id": 25,
    "name": "NEW",
    "last_name": "NEW",
    "email": "new@mail.ru",
    "password": "532442"
    }'

Ответ:

    {
    "user_id": 25,
    "name": "NEW",
    "last_name": "NEW",
    "email": "new@mail.ru",
    "password": "532442"
    }

Вывод в консоли:

    INFO:     127.0.0.1:50128 - "POST /users/ HTTP/1.1" 200 OK

### GET для пользователя

Проверим его в базе: http://127.0.0.1:8000/users/25

Ответ:

    {"user_id":25,"name":"NEW","last_name":"NEW","email":"new@mail.ru","password":"532442"}

Вывод в консоли:

    INFO:     127.0.0.1:50141 - "GET /users/25 HTTP/1.1" 200 OK

### PUT для пользователя

Изменим его:

    curl -X 'PUT' \
    'http://127.0.0.1:8000/users/25' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "user_id": 25,
    "name": "Переименовали",
    "last_name": "string",
    "email": "string@mail.ru",
    "password": "312324"
    }'

Ответ:

    {"user_id":25,"name":"Переименовали","last_name":"string","email":"string@mail.ru","password":"312324"}

Вывод в консоли:

    INFO:     127.0.0.1:50131 - "PUT /users/25 HTTP/1.1" 200 OK

### DELETE для пользователя

А теперь удалим его же:

    curl -X 'DELETE' \
    'http://127.0.0.1:8000/users/25' \
    -H 'accept: application/json'

Ответ:

    {
    "message": "User ID = 25 deleted"
    }

Вывод в консоли:

    INFO:     127.0.0.1:50119 - "DELETE /users/25 HTTP/1.1" 200 OK

## CRUD операции для товаров

### POST для товара

Отправляем запрос:

    curl -X 'POST' \
    'http://127.0.0.1:8000/items/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "item_id": 25,
    "title": "Товар",
    "description": "Новый",
    "price": 200
    }'

Вывод в консоли:

    INFO:     127.0.0.1:49886 - "POST /items/ HTTP/1.1" 200 OK

### GET для товара

http://127.0.0.1:8000/items/25

Ответ:

    {"item_id":25,"title":"Товар","description":"Новый","price":200.0}

Вывод в консоли:

    INFO:     127.0.0.1:49910 - "GET /items/25 HTTP/1.1" 200 OK

### PUT для товара

Отправляем запрос:

    curl -X 'PUT' \
    'http://127.0.0.1:8000/items/25' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "item_id": 25,
    "title": "string",
    "description": "string",
    "price": 11111
    }'

Проверяем: http://127.0.0.1:8000/items/25

Ответ:

    {"item_id":25,"title":"string","description":"string","price":11111.0}

Вывод в консоли:

    INFO:     127.0.0.1:49957 - "GET /items/25 HTTP/1.1" 200 OK

### DELETE для товара

Отправляем запрос:

    curl -X 'DELETE' \
    'http://127.0.0.1:8000/items/25' \
    -H 'accept: application/json'

Ответ:

    {
    "message": "Item ID 25 deleted"
    }

Вывод в консоли:

    INFO:     127.0.0.1:49972 - "DELETE /items/25 HTTP/1.1" 200 OK

## CRUD операции для заказов

### POST для заказа

Отправляем запрос:

    curl -X 'POST' \
    'http://127.0.0.1:8000/orders/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "order_id": 25,
    "user_id": 7,
    "item_id": 5,
    "order_date": "string",
    "status": "string"
    }'

Ответ:

    {
    "order_id": 25,
    "user_id": 7,
    "item_id": 5,
    "order_date": "string",
    "status": "string"
    }

Вывод в консоли:

    INFO:     127.0.0.1:49994 - "POST /orders/ HTTP/1.1" 200 OK

### GET для заказа

Проверяем: http://127.0.0.1:8000/orders/25

    {"order_id":25,"user_id":7,"item_id":5,"order_date":"string","status":"string"}

Вывод в консоли:

    INFO:     127.0.0.1:50012 - "GET /orders/25 HTTP/1.1" 200 OK

### PUT для заказа

Отправляем запрос:

    curl -X 'PUT' \
    'http://127.0.0.1:8000/orders/25' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "order_id": 25,
    "user_id": 1,
    "item_id": 1,
    "order_date": "string",
    "status": "Исполнен"
    }'

Ответ:

    {
    "order_id": 25,
    "user_id": 1,
    "item_id": 1,
    "order_date": "string",
    "status": "Исполнен"
    }

Вывод в консоли:

    INFO:     127.0.0.1:50047 - "PUT /orders/25 HTTP/1.1" 200 OK

### DELETE для заказа

Отправляем запрос:

    curl -X 'DELETE' \
    'http://127.0.0.1:8000/orders/25' \
    -H 'accept: application/json'

Ответ:

    {
    "message": "Order ID = 25 deleted"
    }

Вывод в консоли:

    INFO:     127.0.0.1:50056 - "DELETE /orders/25 HTTP/1.1" 200 OK