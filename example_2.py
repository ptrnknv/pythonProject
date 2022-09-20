def chunked(s, n):
  lst = []
  for i in range(0, len(s), n):
    lst.append(s[i:i+n])
  print(lst)

s = input().split()
n = int(input())

chunked(s, n)