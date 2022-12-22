def recursive_sum(ls):
    if isinstance(ls, int):
        return ls  # базовый случай
    if isinstance(ls, list):
        total = 0
        for i in ls:
            value = recursive_sum(i)
            if value is not None:
                total += value
            else:
                total += 0
        return total


my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
