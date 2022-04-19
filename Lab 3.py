def todo_list():
    import json
    f = open('todo list.json','w+')
    f.close()
    task = []
    n = int(input("Выберите команду:\n1 - Добавить задачу\n2 - Вывести список задач\n3 - Выход"))
    while n!=3 :
        if n == 1:
            name = input('Сформулируйте задачу: ')
            category = input('Добавьте категорию к задаче: ')
            time = input('Добавьте время к задаче: ')
            task.append({"category": category,"name": name, "time": time})
            f = open("todo list.json", "w")
            f.write(json.dumps(task))
            f.close()
        elif n == 2:
            f = open('todo list.json','r')
            tasks = json.load(f)
            f.close()
            for i in tasks:
                print('Задача: ', i["name"], 'Категория: ', i["category"], ' Дата: ', i["time"])
        else:
            print("Такой команды не существует")
    print('задачи сохранены в файл!')

