

mylist = input("Список: ").lower()
a = mylist.split()
print(a)

home = True
while home:
    b = input('добавить или удалить ? ').lower()
    if b == 'добавить':
        s = input('Введите ').lower()
        a.append(s)

        print(a)
    elif b == 'удалить':
        l = input('Введите ').lower()
        a.remove(l)
        print(a)
    elif b =='выход':
        home = False