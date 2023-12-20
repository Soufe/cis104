n = int(input())
integer_list = [int(input()) for _ in range(n)]
count_odd = sum(1 for num in integer_list if num % 2 != 0)
print(count_odd)