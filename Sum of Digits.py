digit = int(input())
while digit >= 10:
    sum = 0
    while digit > 0:
        sum += digit % 10
        digit //= 10
    digit = sum
print(digit)