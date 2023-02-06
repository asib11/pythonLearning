class Person:
    def __init__(self,first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary

    def __repr__(self) -> str:
        return f'{self.first} {self.last} and salary {self.salary}'

    def __add__(self,other):
        return self.salary + other.salary
    
    def __add__(self,other):
        if isinstance(other,Person):
            return Person(self.first ,self.last ,salary= 0)

emp1 = Person('asib', 'ahmed', 20000)
emp2 = Person('tanver','tayeb', 33000)

print(emp1+emp2)