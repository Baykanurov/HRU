import os
from loguru import logger
from helpers.matrix import write_matrix, read_matrix
from helpers.hash import hash_user


@logger.catch()
def create_user(user, password):
    if not os.path.isfile(f'./system/{user}_password'):
        hash_user(user, password)
        matrix = read_matrix()
        matrix[f'./system/{user}_password'] = {user: ['read', 'write', 'own']}
        write_matrix(matrix)
        logger.info(f'Create User "{user}"')
    else:
        logger.error(f'A user with the name "{user}" already exists')
