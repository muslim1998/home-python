import random
def parol(ff):
    c = '1234567890'
    b = 'bsdfvdfwerfds'
    b_2 = 'BUBUHJBYHHNJKNJ'
    s = '@!#%$$&^*'
    pas = ''
    var = [c,b,b_2,s]
    if ff < 12:
        return print('Ошибочка бро! пароль долден быть не менее 12 символов')
    else:
        pas += random.choice(c)
        pas += random.choice(b)
        pas += random.choice(b_2)
        pas += random.choice(s)
        while len(pas)<ff:
            pas += random.choice(var[random.randint(0,3)])
        print(pas)
parol(12)

