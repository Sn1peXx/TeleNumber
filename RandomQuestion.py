import random
import os
import shelve

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento',
'Colorado': 'Denevr', 'Connecticut': 'Hartford', 'Delawaer': 'Dover', 'Florida': 'Tallahassee', 'Monata': 'Helena'}

#Генерация 10 файлов билктов
for quizNum in range(0,10):
	#Создать файлы билетов и ключей
	quizFile = open('D:\\prog\\capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
	#Запись заголовка билета
	quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
	quizFile.write((' ' * 10) + 'Проверка знания столиц штатов (Билет %s)' % (quizNum + 1))
	quizFile.write('\n\n')

	#Перемешать порядок следования штатов
	states = list(capitals.keys())
	random.shuffle(states)

	#Организовать цикл по всем 10 штатам создавая вопрос для каждого из них
	for questionNum in range(5):
		#Получение правильных и не правильных ответов
		correctAnswer = capitals[states[questionNum]]
		wrongAnswer = list(capitals.values())
		del wrongAnswer[wrongAnswer.index(correctAnswer)]
		wrongAnswer = random.sample(wrongAnswer, 3)
		amswerOptions = wrongAnswer + [correctAnswer]
		random.shuffle(amswerOptions)

		quizFile.write('%s. Выбирите столицу штата %s.\n' % (questionNum + 1, states[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], amswerOptions[i]))
		quizFile.write('\n')

			#Запись ключа ответа в файл
		answerKeyFile.write('%s, %s\n' % (questionNum + 1, 'ABCD' [amswerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()