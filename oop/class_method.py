class Car:
    total_car = 0 #class attribute

    def __init__(self, color:str, model:str, seat:int =2, reg=None): #if we dont define datatype, nothing will change
        self.color = color
        self.model = model
        self.__seat = seat #private instance arritibute
        self.__registation = reg
        Car.total_car +=1
    
    def seat(self):
        return self.__seat

    def get_car(self):
        return f'this {self.model} has {self.__seat} setas, color is {self.color} and registration No:{self.__registation if self.__registation is not None else "not registired"}'
    
    def sells_car(self):
        Car.total_car -=1
        return f'{self.model} has sold '

    @classmethod
    def sell_car(cls):
        #Car.total_car -=1
        return f'rest of car is {Car.total_car}'

print(Car.sell_car())
car3 = [Car('blue','BMW',2,1),Car('yellow','BMW',6,2),Car('black','Vlovo',4,3),Car('gray','ford',2),Car('blue','mastang',4),Car('blue','Audi r8',2)]
for i in car3:
    if i.seat() >2:
        print(i.get_car())
        print(i.sells_car())
#print(Car.total_car)
print(Car.sell_car())