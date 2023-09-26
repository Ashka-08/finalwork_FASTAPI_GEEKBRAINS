from app import *
from random import randint, choice


@app.get("/filling_base/{count}")
async def create_base(count: int):
        
    # создание таблицы пользователей
    for i in range(count):
        query_users = users.insert().values(
            user_id = i,
            name = f'user{i}',
            last_name = f'userovskiy{i}',
            email = f'mail{i}@mail.ru',
            password = randint(10000, 100000)
            )
        await database.execute(query_users)

    # создание таблицы пользователей
    for i in range(count):
        query_items = items.insert().values(
            item_id = i,
            title = f'item{i}',
            description = f'description{i}',
            price = randint(100, 1000)
            )
        await database.execute(query_items)

    # создание таблицы заказов
    status_tuple = ('Принят', 'В обработке', 'Оплачен', 'В пути', 'Исполнен')
    for i in range(count):
        query_orders = orders.insert().values(
            order_id = i,
            user_id = randint(0, i),
            item_id = randint(0, i),
            order_date = str(datetime.now),
            status = choice(status_tuple)
            )
        await database.execute(query_orders)
    return {'message': f'{count} users, items and orders create'}
