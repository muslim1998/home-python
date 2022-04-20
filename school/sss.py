import json
def admin_page(on = True,off = False,access = False,teacher={},students={},lessons={},additional={}):
	print('\n----- Добро пожаловать в нашу школу! -----')
	with open('adminparol.json','r')as file:
		data = json.load(file)
	while on:
		login = input('\nВведите логин: ')
		password = input('\nВведите пароль: ')
		for log,pas in data.items():
			if log == login:
				if pas == password:
					access = True
					on = off
					break
				else:
					print('\nНеверный пароль')
		else:
			print('\nПользователь не найден')
	if access:
		print(f'\nДобро пожаловать,{login}!')
		on = access
		while on:
			print('\n1.Создать/редактировать/удалить аккаунт учителя') 
			print('2.Создать/редактировать/удалить аккаунт студента')
			print('3.Создать/редактировать/удалить основные предметы ')
			print('4.Создать/редактировать/удалить дополнительные курсы ')
			print('5.Добавить студента/преподавателя на предмет/дополнительный курс')
			print('6.Сменить аккаунт')
			print('7.Сменить роль')
			action = int(input('\nВыберите опцию: '))
			if action == 1:
				option = int(input('Выберите опцию: (создать - 1, редактировать - 2, удалить  - 3) '))
				if option==1:
					try:
						with open('teachers.json','r',encoding='utf-8') as file:
							teachers_data = json.load(file)
						name = input('Введите имя учителя: ').lower()
						password = input('Введите пароль: ')
						teachers_data[name] = password
						with open('teachers.json','w',encoding='utf-8') as file:
							json.dump(teachers_data,file)
						print('\nАккаунт учителя успешно создан')
					except FileNotFoundError:
						name = input('Введите имя учителя: ').lower()
						password = input('Введите пароль: ')
						teacher[name] = password
						with open('teachers.json','w',encoding='utf-8') as file:
							json.dump(teacher,file)
						print('\nАккаунт учителя успешно создан')
				if option==2:
					try:
						with open('teachers.json','r',encoding='utf-8') as file:
							teachers_data = json.load(file)
						teacher = input('Введите имя учителя: ').lower()
						for teacher_name,password in teachers_data.items():
							if teacher==teacher_name.lower():
								choice = int(input('Что вы хотите изменить? (имя - 1, пароль - 2) '))
								if choice==1:
									new_teacher = input('Введите новое имя учителя: ')
									del teachers_data[teacher_name]
									teachers_data[new_teacher] = password
									with open('teachers.json','w',encoding='utf-8') as file:
										json.dump(teachers_data,file)
									print('\nДанные аккаунта учителя успешно обновлены')
									break
								elif choice==2:
									new_password = input('Введите новый пароль учителя: ')
									teachers_data[teacher_name] = new_password
									with open('teachers.json','w',encoding='utf-8') as file:
										json.dump(teachers_data,file)
									print('\nДанные аккаунта учителя успешно обновлены')
									break
						else:
							print('\nУчитель не найден :/')
					except FileNotFoundError:
						print('\nАккаунты учителей отсутствуют :/')
				if option==3:
					try:
						with open('teachers.json','r',encoding='utf-8') as file:
							teachers_data = json.load(file)
						teacher = input('Введите имя учителя: ').lower()
						for teacher_name in teachers_data.keys():
							if teacher==teacher_name.lower():
								del teachers_data[teacher_name]
								with open('teachers.json','w',encoding='utf-8') as file:
									json.dump(teachers_data,file)
								print('\nАккаунт учителя успешно удалён')
								break
						else:
							print('\nУчитель не найден :/')
					except FileNotFoundError:
						print('\nАккаунты учителей отсутствуют :/')
			if action == 2:
				option = int(input('\nВыберите опцию: создать - 1, редактировать - 2, удалить - 3: '))
				if option == 1:
					try:
						with open('student.json','r')as file:
							student_data = json.load(file)
						name = input('Введите имя учителя: ')
						paswoord = input('Введите пароль: ')
						student_data[name] = password
						with open('student.json','w')as file:
							json.dump(student_data,file)
						print('\nАккаунт студента успешно создан')
					except FileNotFoundError:
						name = input('Введите имя: ').lower()
						password = input('Введите пароль: ')
						students[name] = password
						with open('student.json','w')as file:
							json.dump(students,file)
						print('Вы успешно добавили студента')


					


			
			# 	if option == 2:
			# 		try:
			# 			with open('student.json','r')as file:
			# 				student_data = json.load(file)
			# 			student = input('Введите имя: ').lower()
			# 			for name,password in student_data.items():
			# 				if student == name.lower():
			# 					choice = int(input('Изменить имя - 1, пароль - 2: '))
			# 					if choice == 1:
			# 						new_name = input('Введите новое имя: ').lower()
			# 						del student_data[name]
			# 						student_data[new_name] = password
			# 						with open('student.json','w')as file:
			# 							json.dump(student_data,file)
			# 						print('\nДанные студента изменили')
			# 						break
			# 					elif choice == 2:
			# 						new_password = input('Введите новый пароль: ')
			# 						student_data[name] = new_password
			# 						with open('student.json','w')as file:
			# 							json.dump(student_data,file)
			# 						print('Вы успешно изменили данные!')
			# 						break
			# 			else:
			# 				print('\nСтудент не найден')
			# 		except FileNotFoundError:
			# 			print('\nДанных нет')
			# 	if option == 3:
			# 		try:
			# 			with open('student.json','r')as file:
			# 				student_data = json.load(file)
			# 			student = input('Введите имя учителя: ').lower()
			# 			for name in stident_data.keys():
			# 				if student==teacher_name.lower():
			# 					del student_data[teacher_name]
			# 					with open('student.json','w',encoding='utf-8') as file:
			# 						json.dump(student_data,file)
			# 					print('\nАккаунт учителя успешно удалён')
			# 					break
			# 			else:
			# 				print('\nУчитель не найден :/')
			# 		except FileNotFoundError:
			# 			print('\nАккаунты учителей отсутствуют :/')





								




			
			
				




def students_page():
	print('----------------------------------------------------')
	print()
def teacher_page():
	print('----------------------------------------------------')
	print()




def educational_school(role):
	if role == 1:
		students_page()
	elif role == 2:
		teacher_page()
	elif role == 3:
		admin_page()

role = int(input('Кем вы будете: студент - 1,учитель - 2, админ - 3: '))
educational_school(role)

