import os
from loguru import logger
from helpers.matrix import read_matrix


@logger.catch()
def read_object(user, name):
    if os.path.isfile(f'./system/{name}'):
        matrix = read_matrix()
        if matrix[f'./system/{name}'].get(user) \
                and 'read' in matrix[f'./system/{name}'][user]:
            with open(f'./system/{name}', 'r', encoding="utf-8") as f:
                print(f.read())
            logger.info(f'Access is allowed')
        else:
            logger.error(f'Access denied')
    else:
        logger.error(f'The file with the name "{name}" does not exist')
