import random

num_faces = int(input("サイコロの面の数は?"))  # サイコロの面数(2以上)

if num_faces < 2:
    raise ValueError("サイコロの面数は2以上の必要があります。")

num_rolls = int(input("何回振りますか?"))  # 試行回数


roll_results = [random.randint(1, num_faces) for i in range(1, num_rolls + 1)]
print(roll_results)
