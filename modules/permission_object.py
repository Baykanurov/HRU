import os
from loguru import logger
from helpers.matrix import read_matrix, write_matrix


@logger.catch()
def permission_object(user, new_user, name, permission):
    if os.path.isfile(f'./system/{name}'):
        matrix = read_matrix()
        if '_password' in name:
            logger.error(f'File permissions cannot be changed')
            return
        if not matrix.get(f'./system/{new_user}_password'):
            logger.error(f'The user with the name "{new_user}" does not exist')
            return
        for elem in permission.split(','):
            if elem != 'read' and elem != 'write' and elem != 'own':
                logger.error(f'Invalid argument "{elem}"')
                return
        if matrix[f'./system/{name}'].get(user) \
                and 'own' in matrix[f'./system/{name}'][user]:
            if user == new_user:
                logger.error('Unavailable change')
                return
            matrix[f'./system/{name}'][new_user] = permission.split(',')
            write_matrix(matrix)
            logger.info('Access rights updated')
        else:
            logger.error(f'Access denied')
    else:
        logger.error(f'The file with the name "{name}" does not exist')
