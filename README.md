<h1 align="center">
Реализация модели Харрисона-Рузо-Ульмана с простым набором команд на основе защищенной файловой системы.
</h1>

## Методы
- **Инициализация файловой системы и создание базового пользователя с паролем;**
- **Создание нового пользователя;**
- **Создание нового текстового объекта;**
- **Чтение данных из текстового объекта;**
- **Запись данных в текстовый объект;**
- **Удаление пользователя;**
- **Удаление объекта;**
- **Назначение прав пользователю над объектом.**

Перед началом работы с программой необходимо инициализировать файловой систему (**без объектов - контейнеров**) и создать базового пользователя.

При выполнении любой команды (кроме инициализации) необходимо передать логин и пароль пользователя для аутентификации.\
Проверка пароля осуществляется на основе hash-пароля, который записывается в соответствующий каждому юзеру текстовый файл.

Файловая система инициализируется в директории `./system`.\
Матрица доступа реализована в файле `./system/matrix.json`.

Файл логов создается в директории `./logs`.

Управление зависимостями реализовано с помощью **Poetry**. 

## Доступные права:
- `read` **- Чтение;**
- `write` **- Запись;**
- `own` **- Владение.**


## Примеры команд
>**Инициализация системы**
>- `python hru.py init -l admin -p admin`

>**Создание пользователя**
>- `python hru.py create-user -l admin -p admin -u user1 -up user1_password`

>**Создание объекта**
>- `python hru.py create-object -l admin -p admin -n test_file.txt -c "Тестовый файл"`

>**Чтение данных из объекта**
>- `python hru.py read-object -l admin -p admin -n test_file.txt`

>**Запись данных в объект**
>- `python hru.py write-object -l admin -p admin -n test_file.txt -c "Продолжение тестового файла"`

>**Удаление пользователя**
>- `python hru.py remove-user -l admin -p admin -u user1`

>**Удаление объекта**
>- `python hru.py remove-object -l admin -p admin -n test_file.txt`

>**Назначение прав пользователю над объектом**
>- `python hru.py permission-object -l admin -p admin -u user1 -n test_file.txt -pr "read,write"`
_____________________________
## Контакты:
### Username: Baykanurov
### E-mail: zeevsoffical@gmail.com

