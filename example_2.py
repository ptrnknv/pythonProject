def make_sublist(s):
  lst = [[]]
  for n in range(1, len(s) + 1):
    for i in range(0, len(s) + 1 - n):
      lst.append(s[i:i + n])
  print(lst)


s = '1 2 3 0'.split()

make_sublist(s)
