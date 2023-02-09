import random


def count_elements(list_):
    list_.sort()
    list_.append('')
    counter = 0
    value = list_[0]
    for element in list_:
        if value != element:
            print("Число", value, "встречается", counter, end=" ")
            if 1 < counter < 5:
                print("раза")
            else:
                print("раз")
            counter = 0
            value = element
        counter += 1
    del list_[-1]


my_list = []

for i in range(random.randrange(5, 10)):
    my_list.append(random.randrange(1, 5))

print("Сгенерирован список:", my_list)
count_elements(my_list)
