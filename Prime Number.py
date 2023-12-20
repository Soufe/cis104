x = int(input())
for num in range(2, x):
    prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    if prime:
        print(num)