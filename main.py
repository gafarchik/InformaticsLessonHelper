import time
import os
def start():
	print("█ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █ █▀▀ █▀")
	print("█ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ ░█░ █ █▄▄ ▄█\n")
	print("         █░░ █▀▀ █▀ █▀ █▀█ █▄░█")
	print("         █▄▄ ██▄ ▄█ ▄█ █▄█ █░▀█\n")
	print("        █░█ █▀▀ █░░ █▀█ █▀▀ █▀█")
	print("        █▀█ ██▄ █▄▄ █▀▀ ██▄ █▀▄")
	print("                           by gafarchik")
	time.sleep(3)
	os.system("cls")
	main()

def main():
	ua = ["а","б","в","г","ґ","д","е","є","ж","з","и","і","ї","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ь","ю","я","'"]
	ru = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я","'"]
	eu = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","'"]
	numbers = ["1","2","3","4","5","6","7","8","9","0"]
	try:
		print("Выберите язык")
		print("1) Українська")
		print("2) Русский")
		print("3) English")
		lng = int(input("--> "))
	except ValueError:
		print("OH! It seems you have entered a forbidden character!")
		main()
	if (lng == 1):
		try:
			print("Оберіть дію")
			print("1) Закодувати речення")
			print("2) Декодувати речення")
			print("3) Перетворити число у двійковий код")
			task = int(input("--> "))
			if(task == 1):
				print("Введіть речення")
				sent = str(input("--> "))
				result = ""
				for x in range(0,len(sent)):
					i = sent[x].lower()
					if i in numbers:
						result += str(numbers[numbers.index(i)])
					elif i != " ":
						ch = ua.index(i)+3
						if ch > 34:
							ch -= 34
							result += ua[ch]
						else:
							result += ua[ch]
					else:
						result += " "
				print("Відповідь: " + result)
			if(task == 2):
				print("Введіть речення")
				sent = str(input("--> "))
				result = ""
				for x in range(0,len(sent)):
					i = sent[x].lower()
					if i in numbers:
						result += str(numbers[numbers.index(i)])
					elif i != " ":
						ch = ua.index(i)-3
						if ch <= 0:
							ch += 34
							result += ua[ch]
						else:
							result += ua[ch]
					else:
						result += " "
				print("Відповідь: " + result)
			if(task == 3):
				print("Введіть число")
				num = int(input("--> "))
				res = bin(num)
				print("Відповідь: " + str(res[2::]))
		except ValueError:
			print("ЙОЙ! Здаеться ви ввели заборонений символ!")
			main()
	if(lng == 2):
		try:
			print("Выберите действие")
			print("1) Закодировать предложение")
			print("2) Декодировать предложение")
			print("3) Перевести число в двоичный код")
			task = int(input("--> "))
			if(task == 1):
				print("Введите предложение")
				sent = str(input("--> "))
				result = ""
				for x in range(0,len(sent)):
					i = sent[x].lower()
					if i in numbers:
						result += str(numbers[numbers.index(i)])
					elif i != " ":
						ch = ru.index(i)+3
						if ch > 34:
							ch -= 34
							result += ru[ch]
						else:
							result += ru[ch]
					else:
						result += " "
				print("Ответ: " + result)
			if(task == 2):
				print("Введите предложение")
				sent = str(input("--> "))
				result = ""
				for x in range(0,len(sent)):
					i = sent[x].lower()
					if i in numbers:
						result += str(numbers[numbers.index(i)])
					elif i != " ":
						ch = ru.index(i)-3
						if ch <= 0:
							ch += 34
							result += ru[ch]
						else:
							result += ru[ch]
					else:
						result += " "
				print("Ответ: " + result)
			if(task == 3):
				print("Введите число")
				num = int(input("--> "))
				res = bin(num)
				print("Ответ: " + str(res[2::]))
		except ValueError:
			print("ОЙ! Кажется вы ввели запрещенный символ!")
			main()
	if (lng == 3):
		try:
			print("Choose an action")
			print("1) Encrypt the sentence")
			print("2) Decode sentences")
			print("3) Convert a number to binary code")
			task = int(input("--> "))
			if(task == 1):
				print("Enter the sentence")
				sent = str(input("--> "))
				result = ""
				for x in range(0,len(sent)):
					i = sent[x].lower()
					if i in numbers:
						result += str(numbers[numbers.index(i)])
					elif i != " ":
						ch = eu.index(i)+3
						if ch > 27:
							ch -= 27
							result += eu[ch]
						else:
							result += eu[ch]
					else:
						result += " "
				print("Answer: " + result)
			if(task == 2):
				print("Enter the sentence")
				sent = str(input("--> "))
				result = ""
				for x in range(0,len(sent)):
					i = sent[x].lower()
					if i in numbers:
						result += str(numbers[numbers.index(i)])
					elif i != " ":
						ch = eu.index(i)-3
						if ch <= 0:
							ch += 27
							result += eu[ch]
						else:
							result += eu[ch]
					else:
						result += " "
				print("Answer: " + result)
			if(task == 3):
				print("Enter the number")
				num = int(input("--> "))
				res = bin(num)
				print("Answer: " + str(res[2::]))
		except ValueError:
			print("OH! It seems you have entered a forbidden character!")
			main()
start()
