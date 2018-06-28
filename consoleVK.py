from termcolor import colored
import vk_api
import json
import re
print('Консольный клиент Вконтакте')
def myFriends(vk):
	friendsJS = vk.friends.get()
	friendsJS = json.dumps(friendsJS)
	friendsJS = json.loads(friendsJS)
	friendsId = []
	friendsId = friendsJS['items']
	friendsNum = len(friendsId)
	friendsName = []
	friendsSName = []
	for i in range(friendsNum):
		friendsJS = vk.users.get(user_id = friendsId[i])
		friendsJS = json.dumps(friendsJS)
		friendsJS = json.loads(friendsJS)
		friendsName = friendsJS[0]['first_name']
		friendsSName = friendsJS[0]['last_name']
		print(colored('---------------------\nID друга:','green'), friendsId[i])
		print(colored('Имя:','yellow'),friendsName)
		print(colored('Фамилия:','yellow'),friendsSName)
def myFollowers(vk):
	followersJS = vk.users.getFollowers(count = 1000)
	followersJS = json.dumps(followersJS)
	followersJS = json.loads(followersJS)
	followersId = followersJS['items']
	followersLen = len(followersId)
	for s in range(followersLen):
		followerJS = vk.users.get(user_ids = followersId[s])
		followerJS = json.dumps(followerJS)
		followerJS = json.loads(followerJS)
		followerName = followerJS[0]['first_name']
		followerSName = followerJS[0]['last_name']
		print(colored('-----------------------------------------\nID подписчика:','green'), followersId[s])
		print(colored('Имя:','yellow'),followerName)
		print(colored('Фамилия:','yellow'),followerSName)
def myMessages(vk):
	messagesJS = vk.messages.getConversations()
	messagesJS = json.dumps(messagesJS)
	messagesJS = json.loads(messagesJS)
	messagesId = messagesJS['items']
	messagesNum = len(messagesId)
	messagesName = []
	for a in range(messagesNum):
		messagesId[a] = messagesId[a]['conversation']['peer']['id']
		messagesName = vk.messages.getConversationsById(peer_ids = messagesId[a])
		messagesRE = re.findall(r'.title.', str(messagesName))
		if messagesRE == []:
			messagesName = vk.users.get(user_ids = messagesId[a])
			messagesName = json.dumps(messagesName)
			messagesName = json.loads(messagesName)
			messagesName = colored('Диалог: ','yellow') + messagesName[0]['first_name'] + ' ' + messagesName[0]['last_name']
			print(colored('--------------------------------------------------\nID диалога:','green'), messagesId[a])
			print(messagesName)
		else:
			messagesName = json.dumps(messagesName)
			messagesName = json.loads(messagesName)
			messagesName = colored('Название беседы: ','yellow') + messagesName['items'][0]['chat_settings']['title']
			print(colored('--------------------------------------------------\nID беседы:','green'), messagesId[a])
			print(messagesName)
def myDialogs(vk):
	messagesJS = vk.messages.getConversations()
	messagesJS = json.dumps(messagesJS)
	messagesJS = json.loads(messagesJS)
	messagesId = messagesJS['items']
	messagesNum = len(messagesId)
	messagesName = []
	for a in range(messagesNum):
		messagesId[a] = messagesId[a]['conversation']['peer']['id']
		messagesName = vk.messages.getConversationsById(peer_ids = messagesId[a])
		messagesRE = re.findall(r'.title.', str(messagesName))
		if messagesRE == []:
			messagesName = vk.users.get(user_ids = messagesId[a])
			messagesName = json.dumps(messagesName)
			messagesName = json.loads(messagesName)
			messagesName = colored('Диалог: ','yellow') + messagesName[0]['first_name'] + ' ' + messagesName[0]['last_name']
			print(colored('--------------------------------------------------\nID диалога:','green'), messagesId[a])
			print(messagesName)
def myConversation(vk):
	messagesJS = vk.messages.getConversations()
	messagesJS = json.dumps(messagesJS)
	messagesJS = json.loads(messagesJS)
	messagesId = messagesJS['items']
	messagesNum = len(messagesId)
	messagesName = []
	for a in range(messagesNum):
		messagesId[a] = messagesId[a]['conversation']['peer']['id']
		messagesName = vk.messages.getConversationsById(peer_ids = messagesId[a])
		messagesRE = re.findall(r'.title.', str(messagesName))
		if messagesRE == []:
			nnn = 1
		else:
			messagesName = json.dumps(messagesName)
			messagesName = json.loads(messagesName)
			messagesName = colored('Название беседы: ','yellow') + messagesName['items'][0]['chat_settings']['title']
			print(colored('--------------------------------------------------\nID беседы:','green'), messagesId[a])
			print(messagesName)	
def myHistoryMessages(vk):
	myId = vk.users.get()
	myId = json.dumps(myId)
	myId = json.loads(myId)
	myId = myId[0]['id']
	historyLenStat = 100
	Id = input(colored('Введите ID: ','green'))
	print(colored('\n--------------------------------------','green'))
	historyJS = vk.messages.getHistory(peer_id = int(Id), count = historyLenStat)
	historyJS = json.dumps(historyJS)
	historyJS = json.loads(historyJS)
	historyJS = historyJS['items']
	historyJS = historyJS[::-1]
	historyLen = len(historyJS)
	if historyLen < historyLenStat:
		historyLen = historyLenStat - (historyLenStat - historyLen)
	else:
		historyLen = historyLenStat	
	friendMesJS = []
	friendMesName = []
	for d in range(historyLen):
		friendMesJS = historyJS[d]['from_id']
		friendMesJS = vk.users.get(user_id = friendMesJS)
		friendMesJS = json.dumps(friendMesJS)
		friendMesJS = json.loads(friendMesJS)
		if friendMesJS[0]['id'] == myId:
			friendMesName = colored('Вы:','blue')
		else: 
			friendMesName = colored((friendMesJS[0]['first_name'] + ' ' + friendMesJS[0]['last_name'] + ':'),'yellow')
		print(friendMesName,historyJS[d]['body'])
	print(colored('\n--------------------------------------','green'),colored('\nХотите отправить сообщение сюда?','blue'), colored('\n1) Да.', 'green'),colored('		2) Нет.', 'red'),colored('\n--------------------------------------','green'))
	num = input()
	if int(num) == 1:
		a = True
		while a == True:
			message = input(colored('--------------------------------------------------\nСообщение: ','yellow'))
			try:
				messageID = vk.messages.send(peer_id = int(Id),message = str(message))
			except vk_api.exceptions.ApiError:
				print(colored('Этот пользовватель добавил вас в черный список!','red'))
				a = False
				break
			while True:
				print(colored('\n--------------------------------------','green'),colored('\nЧто вы хотите сделать?','blue'), colored('\n1) Отправить еще одно сообщение.', 'green'),colored('\n2) Изменить сообщение.','green'),colored('\n3) Удалить сообщние.','green'),colored('\n0) Назад.', 'red'),colored('\n--------------------------------------','green'))
				num1 = input()
				if int(num1) == 1:
					break
				elif int(num1) == 2:
					while True:
						print(colored('--------------------------------------------------\nСтарое сообщение: ','blue'), message)
						editMessage = input(colored('Новое сообщение: ','green'))
						editMessageResp = vk.messages.edit(message_id = int(messageID), message = str(editMessage), peer_id = int(Id))
						if int(editMessageResp) == 1:
							print(colored('Успешно отредактированно!!','green'))
							break
						else:
							print(colored('Ошибка!\nПовторите снова!','red'))
							continue
				elif int(num1) == 3:
					while True:
						print(colored('--------------------------------------------------\nУдаляю сообщение!','yellow'))
						try:
							deleteMessage = vk.messages.delete(message_ids = int(messageID),delete_for_all = 1)
						except vk_api.exceptions.ApiError:
							print(colored('Не удалось удалить сообщение для всех','red'))
							print(colored('\n--------------------------------------','green'),colored('\nХотите удалить это сообщение у себя?','blue'),colored('\n1) Да.','green'),colored('		2) Нет.','red'),colored('\n--------------------------------------','green'))
							num2 = input()
							if int(num2) == 1:
								deleteMessage = vk.messages.delete(message_ids = int(messageID),delete_for_all = 0)
							elif int(num2) == 2:
								break
							else:
								print(colored('Некорректное значение!','red'))
								break
						reDeleteMes = re.findall(r'.\b\d+\b..\s', str(deleteMessage))
						reDeleteMes = str(reDeleteMes).replace('[','').replace(']','').replace('"','')
						deleteMessage = str(deleteMessage).replace(str(reDeleteMes),'').replace('{','').replace('}','')
						if int(deleteMessage) == 1:
							print(colored('Успешно удалено!','green'))
							break
						else:
							print(colored('Ошибка!\nУдаляю снова!','red'))
							continue
				elif int(num1) == 0:
					a = False
					break
				else:
					print(colored('Некорректное значение!\nПопробуйте снова!','red'))
					continue
def myAccount(vk):
	accountJS = vk.account.getProfileInfo()
	accountJS = json.dumps(accountJS)
	accountJS = json.loads(accountJS)
	print(colored('-----------------------------------------------------\n','blue'),colored('Имя:','green'),accountJS['first_name'])
	print(colored('-----------------------------------------------------\n','blue'),colored('Фамимлия:','green'),accountJS['last_name'])
	if accountJS['sex'] == 1:
		print(colored('-----------------------------------------------------\n','blue'),colored('Девичья фамилия:','green'),accountJS['maiden_name'])
		print(colored('-----------------------------------------------------\n','blue'),colored('Пол:','green'),'женский')
		if accountJS['relation'] == 1:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'не замужем')
		elif accountJS['relation'] == 2:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'есть друг')
		elif accountJS['relation'] == 3:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'помолвлена')
		elif accountJS['relation'] == 4:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'замужем')
		elif accountJS['relation'] == 5:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'все сложно')
		elif accountJS['relation'] == 6:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'в активном поиске')
		elif accountJS['relation'] == 7:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'влюблена')
		elif accountJS['relation'] == 8:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'в гражданском браке')
		else:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'))
	elif accountJS['sex'] == 2:
		print(colored('-----------------------------------------------------\n','blue'),colored('Пол:','green'),'мужской')
		if accountJS['relation'] == 1:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'не женат')
		elif accountJS['relation'] == 2:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'есть подруга')
		elif accountJS['relation'] == 3:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'помолвлен')
		elif accountJS['relation'] == 4:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'женат')
		elif accountJS['relation'] == 5:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'все сложно')
		elif accountJS['relation'] == 6:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'в активном поиске')
		elif accountJS['relation'] == 7:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'влюблен')
		elif accountJS['relation'] == 8:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'),'в гражданском браке')
		else:
			print(colored('-----------------------------------------------------\n','blue'),colored('Семейное положение:','green'))
	else:
		print(colored('-----------------------------------------------------\n','blue'),colored('Пол:','green'))
	print(colored('-----------------------------------------------------\n','blue'),colored('Страна:','green'),accountJS['country']['title'])
	print(colored('-----------------------------------------------------\n','blue'),colored('Город:','green'),accountJS['city']['title'])
	print(colored('-----------------------------------------------------\n','blue'),colored('Дата рождения:','green'),accountJS['bdate'])
	print(colored('-----------------------------------------------------\n','blue'),colored('Родной город:','green'),accountJS['home_town'])
	print(colored('-----------------------------------------------------\n','blue'),colored('Короткое имя:','green'),accountJS['screen_name'])
	print(colored('-----------------------------------------------------\n','blue'),colored('Статус:','green'),accountJS['status'])
	print(colored('-----------------------------------------------------\n','blue'),colored('Телефон:','green'),accountJS['phone'])
try:
	login = input(colored('Login: ','red'))
	password = input(colored('Password: ','red'))
	print('Подключение.....')
	session = vk_api.VkApi(login, password)
	session.auth()
	vk = session.get_api()
	print('Подключено!')
	while True:
		print(colored('--------------------------\n1) Страница\n2) Друзья\n3) Сообщения','green'),colored('\n0) Выйти','red'),colored('\n--------------------------','green'))
		num = input()
		if int(num) == 1:
			myAccount(vk)
		elif int(num) == 2:
			while True:
				print(colored('--------------------------\n1) Друзья\n2) Подписчики','green'),colored('\n0) Назад', 'red'),colored('\n--------------------------', 'green'))
				num1 = input()
				if int(num1) == 1:
					myFriends(vk)
					print(colored('\n--------------------------------------','green'),colored('\nХотите посмотреть историю сообщений c другом?','blue'), colored('\n1) Да.', 'green'),colored('		2) Нет.', 'red'),colored('\n--------------------------------------','green'))
					num2 = input()
					if int(num2) == 1:
						myHistoryMessages(vk)
					elif int(num2) == 2:
						break
					else:
						print(colored('Некорректное значение.\nПопробуйте снова!', 'red'))
				elif int(num1) == 2:
					myFollowers(vk)
				elif int(num1) == 0:
					break
				else:
					print(colored('Некорректное значение.\nПопробуйте снова!', 'red'))
					continue
		elif int(num) == 3:	
			while True:
				print(colored('--------------------------\n1) Все сообщения\n2) Диалоги\n3) Беседы','green'),colored('\n0) Назад', 'red'),colored('\n--------------------------', 'green'))
				num = input()
				if int(num) == 1:
					myMessages(vk)
				elif int(num) == 2:
					myDialogs(vk)
				elif int(num) == 3:
					myConversation(vk)
				elif int(num) == 0:
					break	
				else:
					print(colored('Некорректное значение.\nПопробуйте снова!', 'red'))
					continue
				while True:
						print(colored('\n--------------------------------------','green'),colored('\nХотите посмотреть историю сообщений?','blue'), colored('\n1) Да.', 'green'),colored('		2) Нет.', 'red'),colored('\n--------------------------------------','green'))
						ist = input()
						if int(ist) == 1:
							myHistoryMessages(vk)
						elif int(ist) == 2:
							break
						else:
							print(colored('Некорректное значение.\nПопробуйте снова!', 'red'))
							continue	
		elif int(num) == 0:
			break
		else:
			print(colored('Некорректное значение.\nПопробуйте снова!', 'red'))
except vk_api.exceptions.BadPassword:
	print(colored('Невреный логин или пароль!','red'))
except vk_api.exceptions.PasswordRequired:
	print(colored('Невреный логин или пароль!','red'))
except KeyboardInterrupt:
	print(colored('\nВыход!','red'))
except ValueError:
	print(colored('Неверное значение!','red'))