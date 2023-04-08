n = int(input("Введите шестизначный номер билета: "))
sum1 = 0
sum2 = 0
for i in range(6):
    num = n % 10
    n = n//10
    if i < 3:
        sum1 = sum1+num
    else:
        sum2 = sum2+num

if sum1 == sum2:
    print ("Билет счастливый")
else:
    print("Билет обычный")

