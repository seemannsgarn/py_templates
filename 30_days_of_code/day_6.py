from audioop import reverse


def foo(string):
    a, b = "", ""
    if len(string) > 1:
        for i in range(len(string)):
            if i%2 == 0:
                a += string[i]
            else:
                b += string[i]
        print(f"{a} {b}")
    else:
        pass

n = int(input())
for i in range(n):
    s = input()
    foo(s)
