import os
from loguru import logger
from helpers.matrix import write_matrix, read_matrix


@logger.catch()
def remove_object(user, name):
    if os.path.isfile(f'./system/{name}'):
        matrix = read_matrix()
        if matrix[f'./system/{name}'].get(user) \
                and 'own' in matrix[f'./system/{name}'][user]:
            os.remove(f'./system/{name}')
            del matrix[f'./system/{name}']
            write_matrix(matrix)
            logger.info(f'File "{name}" deleted')
        else:
            logger.error(f'Access denied')
    else:
        logger.error(f'The file with the name "{name}" does not exist')
