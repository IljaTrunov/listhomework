#spisok=[]
#abc=['a', 'b', 'c']
#slovo="агапчик"
#slovo_list=list(slovo)
#print(slovo)
#print(slovo_list)
#while True :
	#print("Напиши 1, если хочешь добавить букву")
	#print("Напиши 2, если хочешь соединить списки")
	#print("Напиши 3, если хочешь удалить букву или цифру со списка")
	#valik=int(input())
	#if valik==1:
		#a=input("Напиши букву или цифру")
		#slovo_list.append(a)
		#print(f"Добавлено {a}. новое spisok", slovo_list)
	#elif valik==2:
		#slovo_list.extend(abc)
		#print(slovo_list)
	#elif valik==3:
		#a=input("Напиши букву которую хочешь удалить")
		#n=slovo_list.count(a)
		#if n>0: 
			#for i in range(n):
				#slovo_list.remove(a)
		#else:
			#print("Это не буква.")
	#print (slovo_list)

listik=" "
slovo=str(input("Введи слово: "))
slovo1=list(slovo) # делает список
print(slovo,slovo1)
while True:
	listik = int(input("Напиши цифру от 1 до 10 и тебе дадут список"))
	if listik == 1:
		print("В списке",len(slovo1), "символов")#считает длину строки
	        print("Функция len()")
	elif listik == 2:
		if slovo.isalnum()==True: # Состоит ли строка из цифр или букв
			print("Есть символы")
                        print("Функция .isalnum()")
	elif listik == 3:
		if slovo.swapcase()==True: # Переводит символы нижнего регистра в верхний, а верхнего – в нижний
			print(slovo)
			print("Функция .swapcase")
	elif listik == 4:
		if slovo.isspace()==True: # Состоит ли строка из неотображаемых символов
			print("Есть пробел")
		        print("Функция .isspace()")
		else:
			print("Нет пробела")
	elif listik == 5:
		if slovo.isalpha()==True: # Состоит ли строка из букв
			print("В строке есть буква")
		        print("Функция .isalpha()")
		else:
			print("Букв нет")
	elif listik == 6:
		print(slovo.capitalize()) # Переводит первый символ строки в верхний регистр, а все остальные в нижний
	        print("Функция .capitalize()")
	elif listik == 7:
		print(slovo.lower()) # Преобразование строки к нижнему регистру
	        print("Функция .lower()")
	elif listik == 8:
		print(slovo.upper()) # Преобразование строки к верхнему регистру
		print("Функция .upper()")
	elif listik == 9:
		if slovo.istitle()==True: # Начинаются ли слова в строке с заглавной буквы
			print("Есть заглавная буква")
			print("Функция .istitle()")
		else:
			print("Нету заглавной буквы")
	elif listik == 10:
		if slovo.title(): # Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
			print(slovo.title)
		        print("Функция .title()")	
	else:
		print("Неверное значение")
