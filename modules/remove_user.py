import os
from loguru import logger
from helpers.matrix import read_matrix, write_matrix


@logger.catch()
def remove_user(user):
    if os.path.isfile(f'./system/{user}_password'):
        os.remove(f'./system/{user}_password')
        matrix = read_matrix()
        del matrix[f'./system/{user}_password']
        for key, value in matrix.items():
            if value.get(user):
                del matrix[key][user]
        write_matrix(matrix)
        logger.info(f'User "{user}" deleted')
    else:
        logger.error(f'The user with the name "{user}" does not exist')
