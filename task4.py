n = int(input("Введите количество долек по длине: "))
m = int(input("Введите количество долек по ширине: "))
k = int(input("Введите требуемое количество долек: "))
# Сколько всего долек
fullSize = n*m
if (k >= n or k >= m) and k < fullSize and (k % n == 0 or k % m == 0):
    print("Возможно отломить такой кусочек")
else:
    print("Не возможно отломить такой кусочек")
