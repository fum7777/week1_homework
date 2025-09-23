# n*ｍ行列 ver(ndarray)

import numpy as np

# 行列数を入力
n = int(input("行数を入力してください: "))  # 行数
m = int(input("列数を入力してください: "))  # 列数

row = np.arange(1, n + 1)
col = np.arange(1, m + 1)
matrix = np.outer(row, col)

for r in matrix:
    print(*r)

# for文

# row_num = int(input("行数を入力してください: "))  # 行数
# col_num = int(input("列数を入力してください: "))  # 列数

# for i in range(1, row_num + 1):
#     for j in range(1, col_num + 1):
#         print(i * j, end=" ")
#     print()
