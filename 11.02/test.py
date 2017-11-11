# encoding:Utf-8 -*-
import random
times = 10
random1= random.randint(1,10)

p = 0

print('猜猜數字遊戲開始,猜對是天才,猜錯是噗嚨共,共有10次機會:')
temp=input()

while (random1 != p) and (temp > 0) :
 	if temp == random1 :
        print('你猜對了,真是天才',end=' ')
    else:
        print('你猜錯了',end=' ')
    if temp > 0 :
        print('你還有', times-1 , '次機會',end=' ')
    else:
        print('猜了10次都猜不到,你是噗嚨共',end=' ')
    times = times -1
    
	if times > 5 :
    print('成績很好,只猜',10-times,'次就猜到了')
else:    
    print('下次再來,噗嚨共')