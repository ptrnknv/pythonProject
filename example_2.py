def get_all_values(d, key):
    st = set()
    if key in d:
        st.add(d[key])  # базовый случай
    for k, v in d.items():
        if type(v) == dict:
            st.update(get_all_values(v, key))  # рекурсивный случай
    return st

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(result)

