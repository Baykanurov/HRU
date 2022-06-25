import os
from loguru import logger
from helpers.matrix import read_matrix


@logger.catch()
def write_object(user, name, content):
    if os.path.isfile(f'./system/{name}'):
        matrix = read_matrix()
        if matrix[f'./system/{name}'].get(user) \
                and 'write' in matrix[f'./system/{name}'][user]:
            with open(f'./system/{name}', 'a+', encoding="utf-8") as f:
                f.write(f'\n{content}')
            logger.info(f'Access is allowed')
        else:
            logger.error(f'Access denied')
    else:
        logger.error(f'The file with the name "{name}" does not exist')
