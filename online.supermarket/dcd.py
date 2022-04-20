import json 

def user_page(on = True, off = False, cart = {}):
	print('Welocome, user!')
	while on:
		with open('products.json', 'r') as file:
			products = json.load(file)
		print('\n1.Найти продукт')
		print('2.Добавить продукты в корзине')
		print('3.Убрать из корзины')
		print('4.Посмотреть содержимое в корзине')
		print('5.Распечатать текст')
		print('6. Выход')
		action = int(input('\nВведите опции: '))
		if action == 1:
			product = input('\nВведите название продукта: ')
			for item,price in products.items():
				if product == item:
					print(f'\nЦена: - {price}')
					action = input('\nВы хотите добавить данный продукт в корзину: да или нет').lower()
					if action == 'да':
						quantity = int(input('\nВведите количество: '))
						cart[item] = quantity
						with open('cart.json','w') as file:
							json.dump(cart,file)
						print('\nпродукт успешно добавлен в корзину!')
						break
					elif action == 'нет':
						break
						
			else:
				print('\nДанный товар отсутсвует!')
		

		if action == 2:
			product = input('\nВведите название продукта: ')
			for item,price in products.items():
				if product == item:
					quantity = int(input('\nВведите количество: '))
					cart[item] = quantity
					with open('cart.json','w') as file:
						json.dump(cart,file)
					print('\nпродукт успешно добавлен в корзину!')
					break
			else:
				print('\nДанный товар отсутсвует!')

		if action == 3:
			cart_action = int(input('\nУбрать товар из корзины (0) или изменить количество  (1): '))
			if cart_action == 0:
				product = input('\nВведите товар: ')
				for item,quantity in cart.items():
					if product == item:
						del cart[product]
						with open('cart.json','w') as file:
							json.dump(cart,file)
						print('\nПродукт успешно удален!')
						break
				else:
					print('\nДанный товар отсутсвует.')
			elif cart_action == 1:
				product = input('\nВведите название продукта: ')
				for item,quantity in cart.items():
					if product == item:
						new_quantity = int(input('Количество: '))
						cart [item] = new_quantity
						with open('cart.json','w')as file:
							json.dump(cart,file)
						print('\nВы успешно изменили количество: ')
						break
				else:
					print('\nДанный товар отсутсвует')


		if action == 4:
			print('\nМоя корзина')
			for item,quantity in cart.items():
				print(item,quantity)
			print()
		if action == 5:
			overall = []
			print('\nВаш чек: ')
			for stuuf,quantity in cart.items():
				for item,price in products.items():
					if stuuf == item:
						overall_price = quantity * price
						overall.append(overall_price)
						print(f'{item} - {overall_price}')
			print(f'Итого: {sum(overall)}\n')



		if action == 6:
			on = off



def admin_page(on = True,off = False,access = False,n_product = {}):
	with open('admin.json','r') as file:
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
					break
		else:
			print('\nПользователь не найден')
	if access:
		print(f'\nДобро пожаловать , {login}')
		on = access
		while on:
			with open('products.json','r')as file:
				product = json.load(file)
				print('\n1.Найти продукт')
				print('2.Добавить продукт')
				print('3.Удалить продукт')
				print('4.Изменить продукт')
				print('5.Сменить аккаунт')
				print('6.Войти как пользователь')
				print('7.Выход')
				action = int(input('\nВведите опции: '))
				if action == 1:
					products = input('\nВведите название продукта: ')
					for item,price in product.items():
						if products == item:
							print(f'\nЦена: - {price}')
							action = input('\nВы хотите добавить новый продукт? да/нет:  ').lower()
							if action == 'да':
								new_product = input('\nНазвание продукта: ')
								new_price = int(input('\nСтоимость продукта: '))
								product[new_product] = new_price
								with open('products.json','w')as file:
									json.dump(product,file)
								print('\nПродукт успешно добавлен !')
								break
							elif action == 'нет':
								break
				if action == 2:
					products = input('\nВы хотите добавить новый продукт? да/нет:  ').lower()
					if products == 'да':
						new_product = input('\nНазвание продукта: ')
						new_price = int(input('\nСтоимость продукта: '))
						product[new_product] = new_price
						with open('products.json','w')as file:
							json.dump(product,file)
						print('\nпродукт успешно добавлен !')
						break
					elif products == 'нет':
						break
				if action == 3:
					products = input('\nВведите товар который вы хотите удалить: ').lower()
					for item,price in product.items():
						if products == item:
							del product[products]

							with open('products.json','w')as file:
								json.dump(product,file)
							print('\nПродукт успешно удален')
							break
				if action == 4:
					user = input('\nВведите название продукта: ').lower()
					for item,quantity in product.items():
						if user == item:
							new = input('Вы хотите изменить цену или товар? ').lower()
							if new == 'цену':
								new_price = int(input('Введите новую цену: '))
								product [item] = new_price
								with open('products.json','w')as file:
									json.dump(product,file)

								print('Вы изменили цену')
								break
							elif new == 'товар':
								new_product = input('Введите новое название: ')
								product [new_product] =  quantity
								with open('products.json','w')as file:
									json.dump(product,file)
								print('\nВы успешно изменили название')
								break
					else:
						print('\nДанный товар отсутсвует')
					
				if action == 5:
					on = off
					admin_page()									
				if action == 6:
					on = off
					user_page()
			
				if action == 7:
					on = off

					

def start_online_supermarket(role):
	if role == 'u' or role == 'user':
		user_page()
	elif role == 'a' or role == 'admin':
		admin_page()

role = input('Выберите роль: user (u) либо admin (a): ' ).lower()
start_online_supermarket(role)
