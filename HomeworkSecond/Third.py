import random
import string


class Product:
    def __init__(self, name, price, rating, count):
        self.name = str(name)
        self.price = round(float(price), 2)
        self.rating = round(float(rating), 1)
        self.count = int(count)

    def countString(self):
        if 0 < self.count < 11:
            return "В наличии мало"
        elif 10 < self.count < 51:
            return "В наличии немного"
        elif self.count > 50:
            return "В наличии"
        else:
            return "Нет в наличии"


products = []

for i in range(3):
    products.append(
        Product(''.join(random.choice(string.ascii_letters) for m in range(random.randrange(10))),
                random.uniform(10, 1000), random.uniform(0, 5), random.randrange(60)))
    print("Товар", i + 1)
    print("Название:", products[i].name)
    print("Цена:", products[i].price)
    print("Оценка:", products[i].rating)
    print("Наличие:", products[i].countString())
    print()
