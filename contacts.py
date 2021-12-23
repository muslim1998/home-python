a = {'мама': ' 87771111111'}
print('Телефонная книжка:', a)
home = True
while home:
    b = input('добавить/удалить/найти/выход: ').lower()
    if b == 'добавить':
        user = input('Введите имя: ').lower()
        s =  input('Введите номер ').lower()
        a[user] = s
        print('Телефонная книжка: ', a)
    elif b == 'удалить':
        user = input('Введите имя: ').lower()
        del a[user]
        print('Телефонная книжка: ', a)
    elif b == 'найти':
        user = input('Введите имя: ').lower()
        for m,k in a.items():
            if m == user:
                print(f'номер {k}')
    elif b == 'выход':
         home = False