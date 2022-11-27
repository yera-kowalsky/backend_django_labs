# 1 Четные числа
a=int(input('a= '))
b= int(input('b= '))

for num in range(a, b + 1):
    if (num % 2 == 0):
        print(num, end=' ')

# 2 Минимальный делитель
x = int(input())
for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break

# 3 Делители числа
x = int(input('Please, enter a X '))
for i in range(1,x+1):
    if x % i == 0:
      print(i, end=" ")

# 4 Сумма чисел
N = int(input("Enter a N "))
summa = 0
for i in range(N):
    num_2 = int(input("Enter a number "))
    summa+=num_2
print(summa)

# 5 Перевод числа
binary = input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print(decimal)

# 6 Степень
a = int(input("Please enter a base number "))
n = int(input("Please enter a exponent number "))
res = 1
while n != 0:
    res *= a
    n-=1
print(res)

# 7 Голосование
x = int(input("Enter x "))
y = int(input("Enter y "))
z = int(input("Enter z "))
if x+y+z > 1:
    print(1)
else:
    print(0)

# 8