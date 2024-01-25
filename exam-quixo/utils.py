import numpy as np
import sys
from game import Move

def max_sequence(matrix) -> int:
    max_seq_rows = max((max(map(len, ''.join(map(str, row)).split('0'))) for row in matrix), default=0)
    max_seq_columns = max((max(map(len, ''.join(map(str, col)).split('0'))) for col in matrix.T), default=0)
    max_seq_diag = max(
        (max(map(len, ''.join(map(str, np.diag(matrix))).split('0'))),
        max(map(len, ''.join(map(str, np.diag(matrix[:, ::-1]))).split('0')))),
        default=0
    )
    return max(max_seq_rows, max_seq_columns, max_seq_diag)


def encode_move(m):
    s = str(m[0][0])+str(m[0][1])+str(m[1].value)
    s = s.encode('utf-8')
    return s


def decode_move(m):
    m = m.decode('utf-8')
    return (int(m[0]), int(m[1]), Move(int(m[2])))

'''
s = np.float32(40)
print(sys.getsizeof(s))
s = 40.9
print(type(s))
print(sys.getsizeof(s))

matrice = np.array([
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
])

print(sys.getsizeof(str(matrice)))
print(sys.getsizeof('0010101011011100100111001'))
s = np.float16(5.5)
print(sys.getsizeof(s))
s = 5.5
print(sys.getsizeof(s))
'''
