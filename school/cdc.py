import json
student_lessons_new = []
try:
	with open('student.json','r') as file:
		students = json.load(file)
	name = input('Student name: ').lower()
	for student_name in students.keys():
		if name == student_name.lower():
			try:
				with open('test_lessons.json','r') as file:
					lessons = json.load(file)
				lesson = input('Enter lesson: ').lower()
				for lesson_name,number in lessons.items():
					if lesson == lesson_name.lower():
						try:
							with open('test.json','r') as file:
								student_lessons = json.load(file)
							if lesson_name not in student_lessons[student_name]:
								student_lessons[student_name] = student_lessons[student_name].append(lesson_name)
								with open('test.json','w') as file:
									json.dump(student_lessons,file)	
								lessons[lesson_name] = lessons[lesson_name] + 1
								with open('test_lessons.json','w') as file:
									json.dump(lessons,file)
								print('Success')
								break					
							else:
								print('Student already have this lesson')
								break
						except FileNotFoundError:
							student_lessons_new[student_name] = list(lesson_name)
							with open('test.json','w') as file:
								json.dump(student_lessons_new,file)
							lessons[lesson_name] = lessons[lesson_name] + 1
							with open('test_lessons.json','w') as file:
								json.dump(lessons,file)
							print('Success')
							break
						break
				else:
					print('Lesson not found')
					break
			except FileNotFoundError:
				print('No lessons')
				break
	else:
		print('Student not found')
except FileNotFoundError:
	print('No students')