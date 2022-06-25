import hashlib
import uuid


# Создание хеша пароля для пользователя
def hash_user(user, password):
    salt = uuid.uuid4().hex
    hashs = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    with open(f'./system/{user}_password', 'w') as f:
        f.write(f'{hashs}')
