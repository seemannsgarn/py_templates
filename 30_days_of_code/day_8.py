n = int(input())

d = {}
for i in range(n):
    input_string = input().split(" ")
    d[input_string[0]] = input_string[1]

for j in range(n):
    inp = input()
    if inp in d:
        print(f"{inp}={d[inp]}")
    else:
        print("Not found")