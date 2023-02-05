class Person:
    def __init__(self, name, gender) :
        self.name = name
        self.gender = gender

    #def set_name(self,name, gender):


class Student():
    def __init__(self,id, intake):
        self.id = id
        self.intake = intake

class info(Person, Student):
    def __init__(self, name, gender, id , intake):
        Person.__init__(self, name, gender)  
        Student.__init__(self, id, intake)

    @property
    def output_is(self):
        return f'name {self.name}, gender {self.gender}, id {self.id}, intake {self.intake}'

    @output_is.setter
    def output_is(self, given):
        self.name, self.gender, self.id, self.intake = given.split(' ')

a1 = info('asib', 'male', '1', '400')
#a1 = info()
a1.output_is = 'asib male 31 40'
print(a1.output_is)