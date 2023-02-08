import random

random_number = random.randrange(100000)
random_sum = 0

for i in str(random_number):
    random_sum = random_sum + int(i)

print("Случайное число:", random_number)
print("Сумма его цифр:", random_sum)
