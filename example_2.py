def spell(*args):
    dt = [(word[0], len(word)) for word in args]
    res = {}
    for k, v in dt:
        res[k.lower()] = res.get(k.lower(), v) if res.get(k.lower(), v) > v else v
    return res


words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))

# {'р': 7, 'а': 9, 'у': 10, 'к': 5}
# {'м': 10, 'и': 11, 'х': 5, 'б': 8}
# {'f': 8}
