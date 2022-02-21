#1
x=input('Is it raining? ')
x=x.lower()
if x == 'yes':
    y = input('Is it windy? ')
    y = y.lower()
    if y == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')

#2
name = input('Введите имя в нижнем регистре: ').title()
surname = input('Введите фамилию в нижнем регистре: ').title()
print(name + " " + surname)

#3
s = input('Введите первую строку стихотворения: ')
print(len(s))
s1 = int(input("Введите начальную позицию: "))
s2 = int(input("Введите конечную позицию: "))
print(s[s1:s2])

#4
n = input('Введите имя: ')
if len(n) < 5:
    sn = input('Введите фамилию: ')
    print((n + sn).upper())
else:
    print(name.lower())

#5
import math
k = int(input('Введите число, большее 500: '))
print(round(math.sqrt(k), 2))

#6
import math
f =  input('Введите тип фигуры: ')
if f == 'Круг':
    r = float(input('Введите радиус круга: '))
    print('Площадь круга: ', math.pi * r * r)
elif f == 'Треугольник':
    a = float(input('Введите длину стороны А: '))
    b = float(input('Введите длину стороны B: '))
    c = float(input('Введите длину стороны C: '))
    p = (a + b + c)/2
    print('Площадь треугольника: ', math.sqrt(p * (p -a) * (p - b) * (p - c)))
elif f == 'Прямоугольник':
    a = float(input())
    b = float(input())
    print('Площадь прямоугольника: ', a * b)
