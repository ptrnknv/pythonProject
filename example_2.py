
def linear(ls):
    result = []
    for elem in ls:
        if isinstance(elem, list):
            result += linear(elem)
        else:
            result.append(elem)
    return result


my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))
