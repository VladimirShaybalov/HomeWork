class Animal:
    def __init__ (self, name):
        self.alive = True # живой
        self.fed = False  # накормленый
        self.name = name  # индивидуфльное название

class Plant:
    def __init__ (self, name):
        self.edible = False # (съедобность)
        self.name = name    # Индивидуальное название

class Mammal(Animal):
    def eat(self, food):
        if food.edible:     # Проверка на съедобность
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:        # Проверка на съедобность
            print(f'{self.name} съел {food.name}')
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    pass # Цветы не съедобные

class Fruit(Plant):
    def __init__ (self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем как True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов
print(a1.name)  # Вывод: Волк с Уолл-Стрит
print(p1.name)  # Вывод: Цветик семицветик

print(a1.alive)  # Вывод: True
print(a2.fed)    # Вывод: False

# Хищник пытается съесть цветок (несъедобный)
a1.eat(p1)

# Млекопитающее ест фрукт (съедобный)
a2.eat(p2)

print(a1.alive)  # Вывод: False (погиб)
print(a2.fed)    # Вывод: True (насытился)