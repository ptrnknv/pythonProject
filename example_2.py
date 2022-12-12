from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: list(filter(lambda y: y[1] == data[min(data, key=lambda x: data[x])], data.items()))
data.max_values = lambda: list(filter(lambda y: y[1] == data[max(data, key=lambda x: data[x])], data.items()))

data.clear()

data['a'] = 1

print(data.max_values())
print(data.min_values())
