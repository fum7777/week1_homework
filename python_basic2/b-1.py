# 二重for文 ver
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print()


# リスト内包表記 ver
# num_list = [n for n in range(1, 10)]

# for i in range(1, 10):
#     print(*(i * j for j in num_list))


# n*ｍ行列 ver(ndarray)
import numpy as np

n = 9  # n行:row
m = 9  # m列:col

row = np.arange(1, n + 1)
col = np.arange(1, m + 1)

# 列ベクトル * 行ベクトル: outer(a,b) =a * b^T
matrix = np.outer(row, col)

for r in matrix:
    print(*r)
