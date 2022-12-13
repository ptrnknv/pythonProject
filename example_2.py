from collections import Counter


def print_bar_chart(data, mark):
    counter = Counter(data).most_common()
    for k, v in counter:
        print(f'{k.ljust(len(max(data, key=len)))} |{mark * v}')


my_list = ['арбуз', 'черешня', 'клубника', 'арбуз', 'банан', 'Малина', 'малина', 'арбуз', 'арбуз', 'Клубника', 'Банан', 'Малина', 'Черешня', 'Вишня', 'Малина', 'малина', 'Малина', 'Клубника', 'Вишня', 'Клубника']

print_bar_chart(my_list, '@')
