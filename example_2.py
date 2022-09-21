n = int(input())
count = 0

for i in range(n):
    s = input().split()
    avg = int(sum(s)) / len(s)
    if avg > s[i]:
        count += 1

print(count)