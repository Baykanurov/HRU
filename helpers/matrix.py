import json


# Получение матрицы доступа
def read_matrix():
    with open(f'./system/matrix.json', 'r') as f:
        matrix = json.loads(f.read())
    return matrix


# Обновление матрицы доступа
def write_matrix(matrix):
    with open(f'./system/matrix.json', 'w') as f:
        f.write(json.dumps(matrix))
