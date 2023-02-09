import random

my_list = []

for i in range(random.randrange(4, 10)):
    my_list.append(random.randrange(20))

print("1. Сгенерирован список:", my_list)

my_list.sort()

print("2. Список отсортирован:", my_list)

first_half = my_list[:int(len(my_list) / 2):1]
second_half = my_list[:int(len(my_list) / 2) - 1:-1]
my_list.append(random.randrange(20))
my_list_value = my_list[random.randrange(len(my_list))]

print("3.1. Часть списка с положительным шагом:", first_half)
print("3.2. Часть списка с отрицательным шагом:", second_half)
print("4. Добавлен элемент в конец списка:", my_list)
print("5. Длина списка:", len(my_list))
print("6. Положение элемента со значением", str(my_list_value) + ":", my_list.index(my_list_value))
