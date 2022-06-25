import os
import hashlib
from loguru import logger


# Проверка инициализации системы
def check_initialization():
    if os.path.isdir('system'):
        return True
    else:
        logger.error("The system is not initialized")
        return False


# Проверка пароля
def check_password(user, check_pwd):
    if os.path.isfile(f'./system/{user}_password'):
        with open(f'./system/{user}_password', 'r') as f:
            password, salt = f.read().split(':')
            new = hashlib.sha256(salt.encode() + check_pwd.encode()).hexdigest()
            if password == new:
                return True
            else:
                logger.error("Invalid password")
    else:
        logger.error(f"The user with the name {user} does not exist")
