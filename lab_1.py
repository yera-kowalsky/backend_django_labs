# 1. Гипотенуза
a = int(input("a = "))
b = int(input("b = "))
print((a**2+b**2)**0.5)

# 2. Число десятков
a = int(input("Enter the number? "))
print((a//10)%10)

# 3. Следующее четное
a = int(input("Enter the number? "))
print((a+2)-(a%2))

# 4 Конец уроков: ответ нашел в интернете, но сам не смог решить

# 5. Какое из чисел больше?
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(0)

#6. Максимум из трех
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# 7 Ладья
a1 = int(input("координаты ладьи а1:"))
b1 = int(input("координаты ладьи b1:"))
a2 = int(input("координаты другой фигуры a2:"))
b2 = int(input("координаты другой фигуры b2:"))

if a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')

# 8. Существует ли треугольник?
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("NO");
else:
    print("YES");


# 9. Количество равных из трех
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == b and b == c:
    print(3)
elif a == b or b == c:
    print(2)
else:
    print(0)

# 10 Упорядочить три числа
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>b:
    a,b = b,a
print(f'{a} {b} {c}')

