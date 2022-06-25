import os
from loguru import logger
from helpers.matrix import write_matrix
from helpers.hash import hash_user


@logger.catch()
def initialization(user, password):
    if not os.path.isdir('system'):
        os.mkdir('system')
        hash_user(user, password)
        matrix = {f'./system/{user}_password': {user: ['read', 'write', 'own']}}
        write_matrix(matrix)
        logger.info(f'Create user "{user}"')
        logger.info('The system is initialized')
    else:
        logger.error('The system has already been initialized')
        return
