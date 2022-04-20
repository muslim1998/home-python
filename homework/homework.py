# Задача как вывести из строк числа и сложить их (dv343v)

s = input('Введите строку: ')
ls = []

ls_1 = ''

for chet in s:
	if chet.isdigit():
		ls_1 = ls_1 + chet
	else:
		if ls_1 != '':
			ls.append(int(ls_1))
# print(ls)
print(sum(ls))
