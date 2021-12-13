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
slovo=("круТой аГапЧик")
slovo1=list(slovo) # делает список
print(slovo,slovo1)
print("1-функция .len(), которая считает длину строки")
print("2-функция .replace(), которая заменяет слова в значении")
print("3-функция .swapcase() переводит символы нижнего регистра в верхний, а верхнего – в нижний")
print("4-функция .isspace() проверяет состоит ли строка из неотображаемых символов")
print("5-функция .split() раздвляет слова между собой")
print("6-функция .capitalize() переводит первый символ строки в верхний регистр, а все остальные в нижний")
print("7-функция .lower() преобразует строки к нижнему регистру")
print("8-функция .upper() преобразует строки к верхнему регистру")
print("9-функция .istitle() проверяет начинаются ли слова в строке с заглавной буквы")
print("10-функция .ljust(20,"<") заполняет символами")

while True:
	listik = int(input("Напиши цифру от 1 до 10 и я тебе дам рабочую функцию"))
	if listik == 1:
		print(len(slovo)) #считает длину строки
	elif listik == 2:
		print(slovo.replace("круТой аГапЧик","Agapchik is cool")) # Заменяет значение новым значением
	elif listik == 3:
		print(slovo.swapcase()) # Переводит символы нижнего регистра в верхний, а верхнего – в нижний
	elif listik == 4:
		if slovo.isspace()==True: # Состоит ли строка из неотображаемых символов
			print("Есть пробел")
		else:
			print("Нет пробела")
	elif listik == 5:
		print(slovo.split()) #Pаздвляет слова между собой
	elif listik == 6:
		print(slovo.capitalize()) # Переводит первый символ строки в верхний регистр, а все остальные в нижний
	elif listik == 7:
		print(slovo.lower()) # Преобразование строки к нижнему регистру
	elif listik == 8:
		print(slovo.upper()) # Преобразование строки к верхнему регистру
	elif listik == 9:
		if slovo.istitle()==True: # Начинаются ли слова в строке с заглавной буквы
			print("Есть заглавная буква")
		else:
			print("Нету заглавной буквы")
	elif listik == 10:
		print(slovo.ljust(20,"<")) #Заполняет символами
	else:
		print("Неверное значение")
