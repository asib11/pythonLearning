class Person:
    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, given_age):
        if given_age >= 0:
            self._age = given_age
        else:
            self._age = 0

    @property
    def full_name(self):
        return f'{self.first} {self.last} age = {self._age}'       
   
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(' ')

tanveer = Person('tanveer', 'tayeb', -20)
print(tanveer.age)
tanveer.age = 34
print(tanveer.age)
print(tanveer.__dict__)
tanveer.full_name = 'asib ahmed'
print(tanveer.full_name)