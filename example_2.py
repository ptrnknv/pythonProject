import pickle
from sys import stdin


def func(*args):
    return ' '.join(args)


with open('func.pkl', 'wb') as w_file:
    pickle.dump(func, w_file)

func_name, *args = [el.strip() for el in stdin.readlines()]
with open(func_name, 'rb') as file:
    data = pickle.load(file)
    print(data(*args))
