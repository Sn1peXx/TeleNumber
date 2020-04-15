import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{2})
	(\s|-|\.)
	(\d{2})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

# Создать регулярное выражение для адресов электронной почты
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

# Найти соответствия в тексте содержащем в буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append('8 '+ phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Скопировать результаты в буфер обмена 
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Скопировано в буфер обмена')
	print('\n'.join(matches))
else:
	print('Телефнные номера и адреса почты не обнаружены')








