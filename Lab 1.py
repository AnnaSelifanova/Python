#Лабораторная работа 1
documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
#1
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def p(n):
    for i in documents:
        if i['number']== n:
            return 'Владелец документа: '+ i['name']
    return 'Документ не найден в базе'

def s(n):
    for i in directories:
        if n in directories[i]:
            return 'Документ хранится на полке: '+ i
    return 'Документ не найден в базе'

def l():
    for i in documents:
        print(f"№: {i['number']}, тип: {i['type']}, владелец: {i['name']}, {s(i['number'])}")

def ads(n):
    if n in list(directories.keys()):
        print('Такая полка уже существует. Текущий перечень полок: ', list(directories.keys()))
    else:
        directories[n] = []
        print("Полка добавлена. Текущий перечень полок: ", list(directories.keys()))

def ds(n):
    if n in directories.keys():
        if len(directories[n]) == 0:
            del directories[n]
            print('Полка удалена. Текущий перечень полок: ', list(directories.keys()))
        elif len(directories[n]) != 0:
            print('На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: ', list(directories.keys()))
    else:
        print('Такой полки не существует. Текущий перечень полок: ', list(directories.keys()))

def ad(num, type_d, name, directory):
    if directory in directories.keys():
        documents.append({'type': type_d, 'number': num, 'name': name})
        directories[directory] = ['number']
        print('Документ добавлен')
    else:
        print('Такой полки не существует. Добавьте полку командой as.')
    print('Текущий список документов: ')
    l()

def d(n):
    for i in documents:
        if i['number'] == n:
            del i
            print('Документ удален.\nТекущий список докумнтов: ')
        else:
            print('Документ не найден в базе.\nТекущий список документов')
        l()   

def m(number, directory):
    for i in documents:
        if i['number'] == number and directory in list(directories.keys()):
            for j in list(directories.keys()):
                if number in directories[j]:
                    directories[j].remove(number)
                    directories[directory].append(number)
                    print("Документ перемещён.\nТекущий спискок документов:")
                    l()
        elif i['number'] == number and not directory in list(directories.keys()):
            print("Такой полки не существует. Текущий перечень полок: ", list(directories.keys()))
        else:
            print('Документ не найден в базе. \nТекущий список документов: ')
            l()

while True:
    command = input('Введите команду: ')
    if command == 'q':
        break;
    elif command == 'p':
        print(p(input('Введите номер документа: ')))
    elif command == 's':
        print(s(input('Введите номер документа: ')))
    elif command == 'l':
        l()
    elif command == 'ads':
        ads(input('Введите номер полки: '))
    elif command == 'ds':
        ds(input('Введите номер полки: '))
    elif command == 'ad':
        num = input('Введите номер документа: ')
        type_d = input('Введите тип документа: ')
        name = input('Введите владельца документа: ')
        directory = input('Введите полку для хранения: ')
        ad(num, type_d, name, directory)
    elif command == 'd':
        d(input('Введите номер документа: '))
    elif command == 'm':
        number = input('Введите номер документа: ')
        directory = input('Введите номер полки: ')
        m(number, directory)
    else:
        print('Такой команды не существует!')
