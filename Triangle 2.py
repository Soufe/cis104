n = int(input())
for i in range(n):
    space = " " * (n - i - 1)
    star = "*" * (i + 1)
    print(space + star)