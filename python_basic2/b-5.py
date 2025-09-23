num = input("データを入力してください(スペース区切り)")
num_list = list(map(int, num.split()))


def calculate_sum(num_list):
    sum_value = 0
    for i in num_list:
        sum_value += i
    return sum_value


def calculate_max(num_list):
    max_value = num_list[0]
    for i in num_list[1:]:
        if max_value < i:
            max_value = i
    return max_value


def calculate_min(num_list):
    min_value = num_list[0]
    for i in num_list[1:]:
        if min_value > i:
            min_value = i
    return min_value


def calculate_mean(num_list):
    mean_value = calculate_sum(num_list) // len(num_list)
    return mean_value


print(
    f"合計値 {calculate_sum(num_list)}\n"
    f"最大値 {calculate_max(num_list)}\n"
    f"最小値 {calculate_min(num_list)}\n"
    f"平均値 {calculate_mean(num_list)}"
)
