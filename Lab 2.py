def get():
    file = open("students.txt", "r", encoding="utf8")
    lst = file.readlines()
    file.close()
    return lst.sort()

def add_student(surname, name):
    lst = get() 
    student = surname+' '+name
    if student in lst:
        return "Студент уже есть в списке"
    else:
        lst.append(student)
        write(lst)
        return "Студент добавлен!"

def find_student(surname, name = ""):
    lst = get()
    if name != "":
        for i in lst:
            if surname + " " + name in i.strip():
                print(i.strip())
                break
    else:
        for i in lst:
            if surname in i.strip():
                print(i.strip())

def change_student(surname, name, new_surname="", new_name=""):
    lst = get()
    for s in lst:
        if surname in s:
            if name in s:
                index = lst.index(surname + " " + name)
                if new_surname != "":
                    surname = new_surname
                if new_name != "":
                    name = new_name
                lst[index] = surname + " " + name 
                lst.sort()
                write(lst)
                return "Информация изменена!"
    return "Студент не найден"


def delete_student(surname, name = ""):
    lst = read()
    if name != "":
        student = surname+' '+name
        if student in lst:
            lst.remove(student)
            return "Студент удален!"
        else:
            return "Такого студента нет в списке"
    else:
        for s in lst:
            if surname in s:
                print(s)
            name = input("Введите имя")
            for s in lst:
                if name in s:
                    lst.remove(s)
                    write(lst)
                    return "Студент удален"


print('''
add - добавить нового студента
find - найти студента
change - изменить информацию о студенте
delete - удалить студента''')
command = input('Введите команду: ')
if command == 'add':
    print(add_student(input('Введите фамилию: '), input('Введите имя: ')))
elif command == 'find':
    print(find_student(input('Введите фамилию: '), input('Введите имя: ')))
elif command == change:
    print(change_student(input('Введите фамилию: '), input('Введите имя: '), input('Введите новую фамилию: '), input('Введите новое имя: ')))
elif command == delete:
    print(delete_student(input('Введите фамилию: '), input('Введите имя: ')))
else:
    print("Такой команды нет!")
    
    
