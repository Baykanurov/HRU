import os
from loguru import logger
from helpers.matrix import write_matrix, read_matrix


@logger.catch()
def create_object(user, name, content):
    if not os.path.isfile(f'./system/{name}'):
        with open(f'./system/{name}', 'w', encoding="utf-8") as f:
            f.write(content)
        matrix = read_matrix()
        matrix[f'./system/{name}'] = {user: ['read', 'write', 'own']}
        write_matrix(matrix)
        logger.info(f'File "{name}" create')
    else:
        logger.error(f'The file "{name}" already exists')
