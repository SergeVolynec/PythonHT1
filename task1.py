a = int(input("Введите число: "))
sum = 0
while a//10 > 0:
    sum = sum + a % 10
    a = a//10
sum = sum + a
print(sum)
