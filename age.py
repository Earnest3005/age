answer1 = input('請問你有沒有開過車？')
if answer1 == '有':
	answer2 = input('請問你的年齡幾歲？')
	answer2 = float(answer2)
	if answer2 >= 18:
		print('很好')
	else:
		print('你怎麼可以開車？')
elif answer1 == '沒有':
	print('沒你的事了')
else:
	print('只能回答 有/沒有')
