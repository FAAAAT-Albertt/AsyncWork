# a = {"A": 2}
# b = {"B": 3}
# c = a | b
# print(c)

import asyncio

# определние корутины
async def custom_coro():
    pass
    # ожидание другой корутины например
    await asyncio.sleep(1)

# создать корутину
coro = custom_coro()
# проверка типа корутины
print(type(coro))

# главная корутина
async def main():
    # выполнение нашей корутины
    await custom_coro()

# запуск программы, основанной на корутинах
asyncio.run(main())


# создает новый цикл событий asyncio и обеспечивает доступ к нему
loop = asyncio.new_event_loop()

# получает доступ к выполняющемуся циклу событий
loop = asyncio.get_running_loop()

# подождать завершения задачи
"""
await task
"""
# определение корутины под задачи
# Задачу можно создать и запланировать на выполнение только внутри корутины
async def task_coroutine():
    await asyncio.sleep(1)

# создание корутины
coro = task_coroutine()

# создание задачи из корутины
task = asyncio.create_task(coro)

# создание задачи и планирование её выполнения в текущем цикле событий с использованием низкоурвнего апи
task = asyncio.ensure_future(task_coroutine())

"создание объектов таск с использованием low-level api №2"
# получить текущий цикл событий
loop = asyncio.get_event_loop()
# создать задачу и запланировать её выполнение
task = loop.create_task(task_coroutine())


# пример запуска задачи
async def start_task():
    # определяем задачу
    task = asyncio.create_task(start_task())
    # ожидание задачи, что позволяет запуститься ей в корутине
    await task


# проверка на завершение задачи
if task.done():
    # Вернет True при статусе завершено
    # Вернет False при обратном статусе
    pass
