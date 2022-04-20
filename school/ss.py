import json
def admin_page(on = True,off = False,access = False,teacher={},student={},lessons={},additional={},students_new={}):
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
				option = int(input('Выберите опцию:(Создать - 1, редактировать - 2, удалить - 3: '))
				if option == 1:
					try:
						with open('student.json','r') as file:
							student_data = json.load(file)
						name = input('Введите имя: ').lower()
						password = input('Введите пароль: ')
						student[name] = password
						with open('student.json','w')as file:
							json.dump(student,file) 
						print('\nВы успешно добавили студента!')
					except FileNotFoundError:
						name = input('Введите имя: ').lower()
						password = input('Введите пароль: ')
						student[name] = password
						with open('student.json','w')as file:
							json.dump(student,file) 
						print('\nАккаунт успешно добавлен!')
				if option == 2:
					try:
						with open('student.json','r')as file:
							student_data = json.load(file)
						student_name = input('Введите имя: ').lower()
						for name,password in student_data.items():
							if student_name == name.lower():
								choice = int(input('Что вы хотите изменить, имя - 1,пароль - 2: '))
								if choice == 1:
									new_name = input('Введите имя: ').lower()
									del student_data[name]
									student_data[new_name] = password
									with open('student.json','w')as file:
										json.dump(student,file)
									print('\nВы успешно изменили имя')
									break
								elif choice == 2:
									new_password = input('Введите новый пароль: ')
									student_data[name] = new_password
									with open('student.json','w')as file:
										json.dump(student,file)
									print('\nВы успешно изменили пароль')
									break
						else:
							print('\nДанные студента отсутствуют')
					except FileNotFoundError:
						pritn('\nАккаунты не найдены')
				if option == 3:
					try:
						with open('student.json','r')as  file:
							student_data = json.load(file)
						student_name = input('\nВведите имя: ').lower()
						for name,password in student_data.items():
							if student_name == name:
								del student[name]
								with open('student.json','w')as file:
									json.dump(student,file)
								print('\nАккаунт успешно удален')
								break
						else:
							print('\nДанные отсутствуют')
					except FileNotFoundError:
						print('\nАккаунты студента отсутствуют')
			if action == 3:
				option = int(input('Выберите опцию: создать - 1,удалить предмет - 2: '))
				if option == 1:
					try:
						with open('lessons','r')as file:
							lessons_data = json.load(file)
						lessons_new = input('\nВведите предмет: ').lower()
						students = int(input('0'))
						lessons_data[lessons_new] = students
						with open('lessons','w')as file:
							json.dump(lessons_data,file)
						print('\nпредмет успешно добавлен')
					except FileNotFoundError:
						lessons_new = input('\nВведите предмет: ').lower()
						students = int(input('0'))
						lessons[lessons_new] = students
						with open('lessons.json','w')as file:
							json.dump(lessons,file)
						print('\nУспешно добавлен предмет')
				elif option == 2:
					try:
						with open('lessons.json','r')as file:
							lessons_data = json.load(file)
						lessons_new = input('\nПредмет: ').lower()
						for item in lessons_data.keys():
							if lessons_new == item.lower():
								del lessons_data[item]
								with open('lessons.json','w')as file:
									json.dump(lessons_data,file)
								print('\nВы успешно удалили предмет')
						else:
							print('\nПредмет не найден')
					except RuntimeError:
						print('\nВы удалили')
			if action == 4:
				option = int(input('Выберите опцию: создать - 1,удалить предмет - 2,изменить название - 3: '))
				if option == 1:
					try:
						with open('additional','r')as file:
							lessons_data = json.load(file)
						lessons_new = input('\nВведите доп.предмет: ').lower()
						students = int(input('0'))
						lessons_data[lessons_new] = students
						with open('additional','w')as file:
							json.dump(lessons_data,file)
						print('\nпредмет успешно добавлен')
					except FileNotFoundError:
						lessons_new = input('\nВведите предмет: ').lower()
						students = int(input('0'))
						additional[lessons_new] = students
						with open('additional.json','w')as file:
							json.dump(additional,file)
						print('\nУспешно добавлен предмет')
				elif option == 2:
					try:
						with open('additional.json','r')as file:
							lessons_data = json.load(file)
						lessons_new = input('\nПредмет: ').lower()
						for item in lessons_data.keys():
							if lessons_new == item.lower():
								del lessons_data[item]
								with open('additional.json','w')as file:
									json.dump(lessons_data,file)
								print('\nВы успешно удалили предмет')
								break
						else:
							print('\nПредмет не найден')
					except FileNotFoundError:
						print('\nВы удалили')
				elif option == 3:
					try:
						with open('additional.json','r')as file:
							lessons_data = json.load(file)
						n_additional = input('\nВведите  предмет: ').lower()
						for i,j in lessons_data.items():
							if n_additional == i.lower():
								del lessons_data[i]
								new_add = input('\nВведите новый предмет: ').lower()
								lessons_data[new_add]=j
								with open('additional.json','w')as file:
									json.dump(lessons_data,file)
								print('\nВы успешно изменили название предмета!')
								break
						else:
							print('\nДанный предмет отсутствуют')
					except FileNotFoundError:
						pritn('\nДанного предмета нет в базе')


			if action == 5:
				option = int(input('Добавить ученика на предмет - 1,преподавателя - 2, доп.курсы - 3: '))
				if option == 1:
					try:
						with open ('students','r')as file:
							student_data = json.load(file)
						name = input('Введите имя: ').lower()
						for name_students in student_data.keys():
							if name == name_students.lower():
								try:
									with open('lessons.json','r')as file:
										lessons_test = json.load(file)
									lesson = input('\nВведите предмет: ').lower()
									for les,number in lessons_test.items():
										if lesson == les.lower():
											try:
												with open('les_name.json','r')as file:
													student_lessons = json.load(file)
												if les not in student_lessons[name]:
													students_new = student_lessons[name]
													students_new.append(name)
													with open('les_name','w')as file:
														json.dump(students_new,file)
													lessons_test[les] = lessons_test[les] + 1
													with open('lessons.json','w')as file:
														json.dump(lessons_test,file)
													print('Success')
													break
												else:
													print('\nСтудент уже есть на потоке')
													break
											except FileNotFoundError:
												students_new[name] = [les]
												with open('les_name','w')as file:
													json.dump(students_new,file)
												lessons_test[les] = lessons_test[les] + 1
												with open('lessons.json','w')as file:
													json.dump(lessons_test,file)
												print('\nSuccess')
												break
									else:
										print('Lesson not found')
										break
									break
									
								except FileNotFoundError:
									print('\n No lessons')
									break
						else:
							print('cdcd')
					except FileNotFoundError:
						print('no students')


						























			
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



