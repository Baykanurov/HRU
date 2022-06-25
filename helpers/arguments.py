import argparse

parser = argparse.ArgumentParser(description='Model HRU')
subparser = parser.add_subparsers(help='sub-command', dest='cmd')

# Инициализация системы
parser_init = subparser.add_parser('init')
parser_init.add_argument('-l', '--login', help='Login', required=True)
parser_init.add_argument('-p', '--password', help='Password', required=True)

# Создания пользователя
parser_create_user = subparser.add_parser('create-user')
parser_create_user.add_argument('-l', '--login', help='Login', required=True)
parser_create_user.add_argument('-p', '--password', help='Password', required=True)
parser_create_user.add_argument('-u', '--user', help='New user', required=True)
parser_create_user.add_argument('-up', '--user_password', help='New password', required=True)

# Создание объекта
parser_create_object = subparser.add_parser('create-object')
parser_create_object.add_argument('-l', '--login', help='Login', required=True)
parser_create_object.add_argument('-p', '--password', help='Password', required=True)
parser_create_object.add_argument('-n', '--name', help='Name', required=True)
parser_create_object.add_argument('-c', '--content', help='Content', required=True)

# Чтение данных из объекта
parser_read_object = subparser.add_parser('read-object')
parser_read_object.add_argument('-l', '--login', help='Login', required=True)
parser_read_object.add_argument('-p', '--password', help='Password', required=True)
parser_read_object.add_argument('-n', '--name', help='Name', required=True)

# Запись данных в объект
parser_write_object = subparser.add_parser('write-object')
parser_write_object.add_argument('-l', '--login', help='Login', required=True)
parser_write_object.add_argument('-p', '--password', help='Password', required=True)
parser_write_object.add_argument('-n', '--name', help='Name', required=True)
parser_write_object.add_argument('-c', '--content', help='Content', required=True)

# Удаление пользователя
parser_remove_user = subparser.add_parser('remove-user')
parser_remove_user.add_argument('-l', '--login', help='Login', required=True)
parser_remove_user.add_argument('-p', '--password', help='Password', required=True)
parser_remove_user.add_argument('-u', '--user', help='User', required=True)

# Удаление объекта
parser_remove_object = subparser.add_parser('remove-object')
parser_remove_object.add_argument('-l', '--login', help='Login', required=True)
parser_remove_object.add_argument('-p', '--password', help='Password', required=True)
parser_remove_object.add_argument('-n', '--name', help='Name', required=True)

# Выдача прав на объект
parser_access = subparser.add_parser('permission-object')
parser_access.add_argument('-l', '--login', help='Login', required=True)
parser_access.add_argument('-p', '--password', help='Password', required=True)
parser_access.add_argument('-u', '--user', help='User', required=True)
parser_access.add_argument('-n', '--name', help='Name', required=True)
parser_access.add_argument('-pr', '--permission', help='Name', required=True)
