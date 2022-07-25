n = int(input().strip())

n = str(bin(n)[2:]).split("0")
a = 0
for i in n:
    if a < i.count('1'):
        a = i.count('1')
    else:
        continue

    print(a)