import   random

answer = random.randint(1,100)
counter=0
while True:
	counter +=1
	number= int (input('请输入：'))
	if number < answer:
		print ("太小了")
	elif number > answer:
		print ("太大了")
	else:
		print("恭喜猜对了!")
		break
print ('总共猜了%d次'% counter)
if counter > 7:
	print ('你的脑子怕是有问题！')