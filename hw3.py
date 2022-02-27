#1
import random
rand_n = random.randint(1,10)
numder = 0
while rand_n != numder :
    numder = int(input("Введите число: "))
    if numder > rand_n :
       print("Введенное число больше")
    elif numder < rand_n :
        print("Введенное число меньше")
print("Верно!")

#2
def password()->str:
    import random
    len_password = random.randint(7,10)
    new_password = ' '
    for i in range(len_password+1):
        new_password += chr(random.randint(33,126))
    return new_password
print(password())
#3
def check_password(password: str)->bool:
    sum_upper = sum(map(str.isupper, password))
    sum_lower = sum(map(str.islower, password))
    sum_digit = sum(map(str.isdigit, password))
    if len(password) >= 8 and sum_upper > 0 and sum_lower > 0 and sum_digit > 0:
        return True
    else:
        return False
print(check_password(input('Введите пароль: ')))

#4
new = ' '
attempts = 0
while check_password(new) == False:
    new = password()
    attempts += 1
print(f'Пароль: {new} \nКоличество попыток: {attempts}')




