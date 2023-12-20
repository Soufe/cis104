n = int(input())
integer_list = [int(input()) for _ in range(n)]
sorted_list = sorted(integer_list)
for num in sorted_list:
    print(num)