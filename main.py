# a = {"A": 2}
# b = {"B": 3}
# c = a | b
# print(c)

import asyncio
from random import random
import time

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

# проверка на отмену выполнения задачи
if task.cancelled():
    # Вернет True, если задача не была завершена
    # Вернет False в обратном случае
    pass

# получение возвращённого значения из обёрнутой корутины
value = task.result()

# обработка ошибок, при вызове метода result
try:
    # получение возвращённого значения из обёрнутой корутины
    value = task.result()
except Exception:
    # задача завершилась неудачно, результата нет
    pass


# обработка исключения CancelledError
try:
    # получение возвращённого значения из обёрнутой корутины
    value = task.result()
except asyncio.CancelledError:
    # задача была отменена
    pass

# проверка того, не была ли отменена задача
if not task.cancelled():
    # получение возвращённого значения из обёрнутой корутины
    value = task.result()
else:
    # задача была отменена
    pass


# обработка исключения InvalidStateError
try:
    # получение возвращённого значения из обёрнутой корутины
    value = task.result()
except asyncio.InvalidStateError:
    # выполнение задачи ещё не завершено
    pass

# проверка того, завершено ли выполнение задачи
async def coro_test():
    if not task.done():
        await task
    #получение возвращённого значения из обёрнутой корутины
    value = task.result()

# получение исключения, вызванного задачей
exception = task.exception()

# Если задача была отменена — при вызове метода exception() будет выдано исключение CancelledError
try:
    # получение исключения, вызванного задачей
    exception = task.exception()
except asyncio.CancelledError:
    # задача была отменена
    pass

# проверка того, не была ли отменена задача
if not task.cancelled():
    # получение исключения, вызванного задачей
    exception = task.exception()
else:
    # задача была отменена
    pass

# Если выполнение задачи ещё не завершилось — при вызове метода exception() будет выдано исключение InvalidStateError
try:
    # получение исключения, вызванного задачей
    exception = task.exception()
except asyncio.InvalidStateError:
    # выполнение задачи ещё не завершено
    pass


# роверка того, не было ли завершено выполнение задачи
async def coro_test():
    if not task.done():
        await task
    # получение исключения, выданного задачей
    exception = task.exception()

# отмена задачи
was_cancelled = task.cancel()
# вернет True при отмене задачи
# вернет False в обратном случае


# функция-коллбэк, вызываемая после завершения работы задачи
def handle(task):
    print(task)


# регистрация коллбэка
task.add_done_callback(handle)
#удаление коллбэка, вызываемого при завершении задачи
task.remove_done_callback(handle)

# создание задачи из корутины с заданием имени
task = asyncio.create_task(task_coroutine(), name='MyTask')

# назначение задаче имени
task.set_name('MyTask')

# получение имени задачи
name = task.get_name()

# получение текущей задачи
task = asyncio.current_task()


# пример получения текущей задачи из главной корутины
# определение главной корутины
async def main():
    # вывод сообщения
    print('main coroutine started')
    # получение текущей задачи
    task = asyncio.current_task()
    # вывод сведений о ней
    print(task)
# запуск asyncio-программы
asyncio.run(main())

# получение всех задач
tasks = asyncio.all_tasks()

# пример, где запускают множество задач, а после этого получают к ним доступ
# корутина для задач
async def task_coroutine(value):
    # вывод сообщения
    print(f'task {value} is running')
    # краткая блокировка
    await asyncio.sleep(1)
# определение главной корутины
async def main():
    # вывод сообщения
    print('main coroutine started')
    # запуск нескольких задач
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    # выделение времени, необходимого на то, чтобы некоторые из задач запустились
    await asyncio.sleep(0.1)
    # получение всех задач
    tasks = asyncio.all_tasks()
    # вывод сведений обо всех задачах
    for task in tasks:
        print(f'> {task.get_name()}, {task.get_coro()}')
    # ждём завершения всех задач
    for task in started_tasks:
        await task
# запуск asyncio-программы
asyncio.run(main())


# выполнение коллекции объектов, допускающих ожидание
async def gather_coro(coro1, coro2):

    results = await asyncio.gather(coro1(), asyncio.create_task(coro2()))

    # выполнение нескольких корутин
    asyncio.gather(coro1(), coro2()) # ТАК МОЖНО!

    # функции нельзя передать напрямую список объектов, допускающих ожидание
    asyncio.gather([coro1(), coro2()]) # ТАК НЕЛЬЗЯ!

    # вызов функции с передачей ей распакованного списка объектов, допускающих ожидание
    asyncio.gather(*[coro1(), coro2()])

    # получение объекта Future, который представляет несколько объектов, допускающих ожидание
    group = asyncio.gather(coro1(), coro2())
    # приостановка работы и ожидание в течение некоторого времени, чтобы дать группе объектов возможность выполниться
    await asyncio.sleep(10)
    # выполнение группы объектов, допускающих ожидание
    await group

    # выполнение группы объектов, допускающих ожидание, и получение возвращаемых значений
    results = await group

    # однострочный вариант запуска задач и получения результатов
    results = await asyncio.gather(coro1(), coro2())


# пример запуска с помощью gather() множества корутин, находящихся в списке
# корутина, используемая для создания задач
async def task_coro(value):
    # вывод сообщения
    print(f'>task {value} executing')
    # приостановка работы на некоторое время
    await asyncio.sleep(1)

# корутина, используемая в роли точки входа в программу
async def main():
    # вывод сообщения
    print('main starting')
    # создание множества корутин
    coros = [task_coro(i) for i in range(10)]
    # выполнение задач
    await asyncio.gather(*coros)
    # вывод сообщения
    print('main done')

# запуск asyncio-программы
asyncio.run(main())


# пример ожидания завершения всех задач
# корутина, которая будет выполняться в новой задаче
async def task_coro(arg):
    # генерирование случайного значения в диапазоне между 0 и 1
    value = random()
    # блокировка на некоторое время
    await asyncio.sleep(value)
    # вывод значения
    print(f'>task {arg} done with {value}')

# главная корутина
async def main():
    # создание нескольких задач
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # ожидание завершения выполнения всех задач
    done,pending = await asyncio.wait(tasks)
    # вывод результатов
    print('All done')

# запуск asyncio-программы
asyncio.run(main())



# пример ожидания выполнения корутины с тайм-аутом
# корутина, которая будет выполняться в новой задаче
async def task_coro(arg):
    # генерирование случайного значения в диапазоне между 1 и 2
    value = 1 + random()
    # вывод сообщения
    print(f'>task got {value}')
    # блокировка на некоторое время
    await asyncio.sleep(value)
    # вывод сообщения о завершении работы
    print('>task done')

# главная корутина
async def main():
    # создание задачи
    task = task_coro(1)
    # запуск задачи и ожидание её завершения с тайм-аутом
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print('Gave up waiting, task canceled')

# запуск asyncio-программы
asyncio.run(main())


# создание задачи
task = asyncio.create_task(coro())
# создание объекта, включающего в себя задачу и защищающего её от отмены
shield = asyncio.shield(task)
# отмена выполнения защитного объекта (задача при этом не отменяется)
shield.cancel()


# пример использования функции asyncio.shield() для защиты задачи от отмены
# определение простой корутины
async def simple_task(number):
    # блокировка на некоторое время
    await asyncio.sleep(1)
    # возврат аргумента
    return number

# корутина, отменяющая переданную ей задачу через некоторое время
async def cancel_task(task):
    # блокировка на некоторое время
    await asyncio.sleep(0.2)
    # отмена задачи
    was_cancelled = task.cancel()
    print(f'cancelled: {was_cancelled}')

# главная корутина
async def main():
    # создание корутины
    coro = simple_task(1)
    # создание задачи
    task = asyncio.create_task(coro)
    # создание защищённой задачи
    shielded = asyncio.shield(task)
    # создание задачи, отменяющей переданную ей задачу
    asyncio.create_task(cancel_task(shielded))
    # обработка отмены
    try:
        # ожидание завершения работы защищённой задачи
        result = await shielded
        # вывод сведений о полученных результатах
        print(f'>got: {result}')
    except asyncio.CancelledError:
        print('shielded was cancelled')
    # ожидание
    await asyncio.sleep(1)
    # вывод сведений о задачах
    print(f'shielded: {shielded}')
    print(f'task: {task}')

# запуск программы
asyncio.run(main())


# пример выполнения блокирующей задачи, зависящей от подсистемы ввода/вывода, в asyncio
# блокирующая задача, зависящая от подсистемы ввода/вывода
def blocking_task():
    # вывод сообщения
    print('Task starting')
    # блокировка на некоторое время
    time.sleep(2)
    # вывод сообщения
    print('Task done')

# главная корутина
async def main():
    # вывод сообщения
    print('Main running the blocking task')
    # создание корутины для блокирующей задачи
    coro = asyncio.to_thread(blocking_task)
    # планирование задачи
    task = asyncio.create_task(coro)
    # вывод сообщения
    print('Main doing other things')
    # позволяем запланированной задаче запуститься
    await asyncio.sleep(0)
    # ожидание завершения задачи
    await task

# запуск asyncio-программы
asyncio.run(main())


# определение асинхронного итератора
class AsyncIterator():
    # конструктор, объявление некоторых данных, относящихся к состоянию объекта
    def __init__(self):
        self.counter = 0

    # создание экземпляра итератора
    def __aiter__(self):
        return self

    # возврат следующего объекта, допускающего ожидание
    async def __anext__(self):
        # проверка на то, есть ли ещё невозвращённые элементы
        if self.counter >= 10:
            raise StopAsyncIteration
        # инкрементирование счётчика
        self.counter += 1
        # возврат значения счётчика
        return self.counter


# пример работы с асинхронным итератором с применением цикла async for
# определение асинхронного итератора
class AsyncIterator():
    # конструктор, объявление некоторых данных, относящихся к состоянию объекта
    def __init__(self):
        self.counter = 0

    # создание экземпляра итератора
    def __aiter__(self):
        return self

    # возврат следующего объекта, допускающего ожидание
    async def __anext__(self):
        # проверка на то, есть ли ещё невозвращённые элементы
        if self.counter >= 10:
            raise StopAsyncIteration
        # инкрементирование счётчика
        self.counter += 1
        # имитация работы
        await asyncio.sleep(1)
        # возврат значения счётчика
        return self.counter

# главная корутина
async def main():
    # обход асинхронного итератора с помощью цикла async for
    async for item in AsyncIterator():
        print(item)

# выполнение asyncio-программы
asyncio.run(main())


# определение асинхронного генератора
async def async_generator():
    for i in range(10):
        yield i


# пример использования асинхронного генератора в цикле async for
# определение асинхронного генератора
async def async_generator():
    # обычный цикл
    for i in range(10):
        # блокировка, имитирующая выполнение работы
        await asyncio.sleep(1)
        # выдача результата
        yield i

# главная корутина
async def main():
    # обход асинхронного генератора с помощью цикла async for
    async for item in async_generator():
        print(item)

# выполнение asyncio-программы
asyncio.run(main())


# определение асинхронного менеджера контекста
class AsyncContextManager:
    # вход в асинхронный менеджер контекста
    async def __aenter__(self):
        # вывод сообщения
        print('>entering the context manager')
        # блокировка на некоторое время
        await asyncio.sleep(0.5)

    # выход из асинхронного менеджера контекста
    async def __aexit__(self, exc_type, exc, tb):
        # вывод сообщения
        print('>exiting the context manager')
        # блокировка на некоторое время
        await asyncio.sleep(0.5)


# пример работы с асинхронным менеджером контекста и с async with
# определение асинхронного менеджера контекста
class AsyncContextManager:
    # вход в асинхронный менеджер контекста
    async def __aenter__(self):
        # вывод сообщения
        print('>entering the context manager')
        # блокировка на некоторое время
        await asyncio.sleep(0.5)

    # выход из асинхронного менеджера контекста
    async def __aexit__(self, exc_type, exc, tb):
        # вывод сообщения
        print('>exiting the context manager')
        # блокировка на некоторое время
        await asyncio.sleep(0.5)

# определение простой корутины
async def custom_coroutine():
    # создание и использование асинхронного менеджера контекста
    async with AsyncContextManager() as manager:
        # вывод результирующего сообщения
        print(f'within the manager')

# запуск asyncio-программы
asyncio.run(custom_coroutine())

# синхронные примеры
# создание списка с использованием спискового включения
result = [a*2 for a in range(100)]
# создание словаря с использованием comprehension-выражения
result = {a:i for a,i in zip(['a','b','c'],range(3))}
# создание множества с использованием comprehension-выражения
result = {a for a in [1, 2, 3, 2, 3, 1, 5, 4]}

async def agenerator(): # просто пример, код реализован не верно

# асинхронное списковое включение, в котором используется асинхронный генератор
    result = [a async for a in agenerator]

async def awaitables(): # просто пример, код реализован не верно

# списковое включение с выражением await и обработка коллекции объектов, допускающих ожидание
    results = [await a for a in awaitables]


# пример выполнения команды в подпроцессе в asyncio-программе
# главная корутина
async def main():
    # начало выполнения команды в подпроцессе
    process = await asyncio.create_subprocess_exec('echo', 'Hello World')
    # вывод сведений о подпроцессе
    print(f'subprocess: {process}')

# точка входа в программу
asyncio.run(main())


# пример выполнения команды командной оболочки в asyncio-программе в виде подпроцесса
# главная корутина
async def main():
    # начало выполнения команды командной оболочки в подпроцессе
    process = await asyncio.create_subprocess_shell('echo Hello World')
    # вывод сведений о подпроцессе
    print(f'subprocess: {process}')

# точка входа в программу
asyncio.run(main())

async def coro_server(): # просто пример, код выполнен не верно
# открытие соединения с HTTP-сервером
    reader, writer = await asyncio.open_connection('www.google.com', 80)

# функция для обработки клиентских подключений
async def handler(reader, writer): # просто пример, код выполнен не верно

    # запуск сервера, предназначенного для приёма HTTP-соединений
    server = await asyncio.start_server(handler, '127.0.0.1', 80)


"""
# запись побайтного представления данных
writer.write(byte_data)
# запись нескольких строк побайтного представления данных
writer.writelines(byte_lines)
# запись байтового представления данных
writer.write(byte_data)
# ожидание завершения передачи данных
await writer.drain()
# чтение байтового представления данных
byte_data = await reader.read()
# чтение байтового представления данных
byte_data = await reader.read(n=100)
# чтение строки данных
byte_line = await reader.readline()
# закрытие сокета
writer.close()

"""