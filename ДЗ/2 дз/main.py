from abc import ABC, abstractmethod


class creature(ABC):
    def __init__(self, name, age, breed, gender):
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender

    @abstractmethod
    def makesound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Animal(creature):

    def birthday(self):
        self.age += 1
        print("Теперь " + self.name + "стал на год старше")


class Cat(Animal):

    def makesound(self):
        print("МЯЯЯЯЯЯЯЯЯЯЯУУУУУУУУУУУУУ")

    def move(self):
        if (self.gender == "Ж"):
            for i in range(5):
                print("Кошка " + self.name + " идёт", end=' ,')
            print("Кошка остановилась")
        else:
            for i in range(5):
                print("Кот " + self.name + " идёт", end=' ,')
            print("Кот остановился")

    def popa(self):
        print("popa")

    def birthday(self):
        print("Появилось больше усов")
        self.age += 1
        print("Теперь " + self.name + "стал на год старше")


class Dog(Animal):

    def makesound(self):
        print("ГАФ")

    def move(self):
        for i in range(5):
            print("Собака " + self.name + " идёт", end=' ,')
        print("Собака остановился")


def getyears(a):
    if (a.age == 1):
        years = " год"
    elif (a.age > 1 and a.age < 5):
        years = " года"
    else:
        years = " лет"
    return years


if __name__ == '__main__':
    a = Cat("Чувапсис", 1, "Манчкин", "Ж")
    a.move()
    a.makesound()
    print("Сейчас " + a.name + "у " + str(a.age) + getyears(a))
    a.birthday()
    print("Сейчас " + a.name + "у " + str(a.age) + getyears(a))

    b = Dog("Дымыч", 3, "Дварняга", "М")
    b.move()
    b.makesound()
    print("Сейчас " + b.name + "у " + str(b.age) + getyears(b))
    b.birthday()
    print("Сейчас " + b.name + "у " + str(b.age) + getyears(b))

    b.makesound()
    a.makesound()