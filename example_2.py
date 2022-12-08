import string


eng_alpha = string.ascii_lowercase
given_alpha = input()
st = input()
print(st.lower().translate(st.maketrans(eng_alpha, given_alpha)))
