# import json


# def func(places={"England": {}, "France": {}, "Channel": {}},place=[]):
# 	n = True
# 	while n:
# 		s = input()
# 		place.append(s)
# 		if s=='':
# 			n = False
# 	for i in place:
# 		for key,dic in places.items():
# 			if i.split(', ')[0]==key:
# 				if i.split(', ')[1] in dic.keys():
# 					dic[i.split(', ')[1]] = dic[i.split(', ')[1]] + int(i.split(', ')[2])
# 				else:
# 					dic[i.split(', ')[1]] = int(i.split(', ')[2])
# 	with open('observations.json', 'w') as file:
# 		json.dump(places,file)
# 	print('-------- Done --------')
# func()

# def human_read_format(size):
# 	if  size < 1024:
# 		return str(size) + 'Б'
# 	elif 1024 < size <= 1024 ** 2:
# 		return str(round(size / 1024)) + 'КБ'
# 	elif 1024 ** 2 < size <= 1024 ** 3:
# 		return str(round(size / 1024 ** 2)) + 'МБ'
# 	return str(round(size / 1024 ** 3)) + 'ГБ'

# print(human_read_format(1500000000))