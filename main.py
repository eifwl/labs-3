class players:
    def __init__(self, age, height, weight, speed):
        self.age = age
        self.height = height
        self.weight = weight
        self.speed = speed

    def setings(self):
        print(
            f'його вік {self.age} років, його ріст {self.height} см, його вага {self.weight} кг, його швидкість {self.speed} км/год')


class players_1(players):
    def __init__(self, age, height, weight, speed, defence):
        super().__init__(age, height, weight, speed)
        self.defence = defence

    def setings(self):
        print(
            f'його вік {self.age} років, його ріст {self.height} см, його вага {self.weight} кг, його швидкість {self.speed} км/год, його захист {self.defence} гравців')


class players_2(players):
    pass


p1 = players_1('22', '185', '80', '35', '8/10')
p1.setings()
p2 = players_2('21', '179', '59', '34', )
p2.setings()

