import random
rNum = random.randrange(100000)
rSum = 0
for i in str(rNum):
    rSum = rSum + int(i)
print("Случайное число: ", rNum)
print("Сумма его цифр: ", rSum)
