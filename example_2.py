import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        res = []
        for el in objects:
            if type(el) == typename:
                res.append(el)
        pickle.dump(res, file)


filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)


with open('numbers.pkl', 'rb') as reader:
    print(pickle.load(reader))
