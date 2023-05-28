# Python Тестовое задние

Этот репозиторий содержит решение предложенных задач на Python, а также файл "requirements.txt" для установки необходимых зависимостей проекта.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.x. Если нет, [скачайте и установите Python](https://www.python.org/downloads/).

2. Создайте виртуальное окружение для изоляции зависимостей. Откройте командную строку (терминал) и выполните следующую команду:

   ```shell
   python -m venv myenv

3. Активируйте виртуальное окружение.

   ```shell
   myenv\Scripts\activate
 
4. Установите зависимости проекта, перейдя в корневую директорию проекта и выполнив команду:

     ```shell
   pip install -r requirements.txt
   
## Простые числа

Решение по поиску простых чисел с квадратичной оптимизацией. Корневой файл "main.py", a также тестовые примеры "test.py" расположенны в следующей директорий. 

     ```shell
   cd tasks/prime_numbers/ && python3 main.py 42
   
  Где "42" является примером ввода для поиска простых чисел 
  
## Выкачивание кода страниц

В данном решении были использованны следующие библиотеки asyncio/aiohttp для асинхронной обработки запросов по указанным ссылкам - директория списка ссылок "tasks/url_upload/urls.txt". Далее, создан сценарий работы модуля и произведен unittest.TestCase в файле "test.py". Запуск производится следующей командой. 

     ```shell
   cd tasks/url_upload/ && python3 main.py
