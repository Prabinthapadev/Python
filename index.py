class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def start(self):
        print(f"{self.color} {self.brand} is starting ")
my_car = Car("tesla","black")
my_car.start()
