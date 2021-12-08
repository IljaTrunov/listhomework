spisok=[]
abc=['a', 'b', 'c']
slovo="агапчик"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True :
	print("Напиши 1, если хочешь добавить букву")
	print("Напиши 2, если хочешь соединить списки")
	print("Напиши 3, если хочешь удалить букву или цифру со списка")
	valik=int(input())
	if valik==1:
		a=input("Напиши букву или цифру")
		slovo_list.append(a)
		print(f"Добавлено {a}. новое spisok", slovo_list)
	elif valik==2:
		slovo_list.extend(abc)
		print(slovo_list)
	elif valik==3:
		a=input("Напиши букву которую хочешь удалить")
		n=slovo_list.count(a)
		if n>0: 
			for i in range(n):
				slovo_list.remove(a)
		else:
			print("Это не буква.")
	print (slovo_list)

