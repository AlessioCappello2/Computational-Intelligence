import numpy as np

'''matrice_o = np.array([
    [-1, 0, 1, 0, 1],
    [-1, 1, -1, 1, 1],
    [-1, 1, 1, 1, 0],
    [-1, 1, 0, 0, 1],
    [1, 1, -1, 0, 1]
])

m = np.where(matrice_o == 1, 1, 0)
print(m)

matrice = np.array([
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
])

# Trova la successione più lunga di 1 nelle righe
max_successione_righe = max((max(map(len, ''.join(map(str, row)).split('0'))) for row in matrice), default=0)

# Trova la successione più lunga di 1 nelle colonne
max_successione_colonne = max((max(map(len, ''.join(map(str, col)).split('0'))) for col in matrice.T), default=0)

# Trova la successione più lunga di 1 nelle diagonali principali
max_successione_diagonali_principali = max(
    (max(map(len, ''.join(map(str, np.diag(matrice))).split('0'))),
     max(map(len, ''.join(map(str, np.diag(matrice[:, ::-1]))).split('0')))),
    default=0
)

# Stampa i risultati
print("Successione più lunga di 1 nelle righe:", max_successione_righe)
print("Successione più lunga di 1 nelle colonne:", max_successione_colonne)
print("Successione più lunga di 1 nelle diagonali principali:", max_successione_diagonali_principali)'''

def max_sequence(matrix) -> int:
    max_seq_rows = max((max(map(len, ''.join(map(str, row)).split('0'))) for row in matrix), default=0)
    max_seq_columns = max((max(map(len, ''.join(map(str, col)).split('0'))) for col in matrix.T), default=0)
    max_seq_diag = max(
        (max(map(len, ''.join(map(str, np.diag(matrix))).split('0'))),
        max(map(len, ''.join(map(str, np.diag(matrix[:, ::-1]))).split('0')))),
        default=0
    )
    return max(max_seq_rows, max_seq_columns, max_seq_diag)