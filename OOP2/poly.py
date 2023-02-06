class Person:
    def slary(self):
        raise NotImplementedError('no salary pass')

class ManagementDept(Person): 
    def salary(self): #polymorphism
        return 'got salary'

class ItDept(Person):
    def salary(self): #polymorphism
        return 'engineer got salary'

m = ManagementDept()
print(m.salary())
p = Person()
print(p.slary())