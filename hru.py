import os
from loguru import logger
from helpers.arguments import parser
from helpers.check import check_password, check_initialization
from modules.init import initialization
from modules.create_user import create_user
from modules.remove_user import remove_user
from modules.create_object import create_object
from modules.remove_object import remove_object
from modules.read_object import read_object
from modules.write_object import write_object
from modules.permission_object import permission_object

args = parser.parse_args()

logger.add('./logs/debug.log',
           format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
           rotation='10 MB',
           colorize=True,
           encoding="utf-8")

if __name__ == "__main__":
    if not os.path.isdir('logs'):
        os.mkdir('logs')

    # Инициализация системы
    if args.cmd == 'init':
        initialization(args.login, args.password)

    # Создания пользователя
    elif args.cmd == 'create-user' \
            and check_initialization() \
            and check_password(args.login, args.password):
        create_user(args.user, args.user_password)

    # Создание объекта
    elif args.cmd == 'create-object' \
            and check_initialization() \
            and check_password(args.login, args.password):
        create_object(args.login, args.name, args.content)

    # Чтение данных из объекта
    elif args.cmd == 'read-object' \
            and check_initialization() \
            and check_password(args.login, args.password):
        read_object(args.login, args.name)

    # Запись данных в объект
    elif args.cmd == 'write-object' \
            and check_initialization() \
            and check_password(args.login, args.password):
        write_object(args.login, args.name, args.content)

    # Удаление объекта
    elif args.cmd == 'remove-object' \
            and check_initialization() \
            and check_password(args.login, args.password):
        remove_object(args.login, args.name)

    # Удаление пользователя
    elif args.cmd == 'remove-user' \
            and check_initialization() \
            and check_password(args.login, args.password):
        remove_user(args.user)

    elif args.cmd == 'permission-object'\
            and check_initialization() \
            and check_password(args.login, args.password):
        permission_object(args.login, args.user, args.name, args.permission)

