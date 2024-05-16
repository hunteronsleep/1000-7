import time
x = 1000
while x>7:
    print(x, "-7", x-7, sep="")
    time.sleep(0.03)
    x-=7
if x<7:
    print('Я гуль!!!')
    print("У МЕНЯ НЕТ ПРОБЛЕМ, КРОМЕ МОЕЙ БОШКИ 1000-7. Я УМЕР ПРОСТИ")
