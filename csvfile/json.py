import jsonpickle

class Man:
    def __init__(self, first, last):
        self.first = first
        self.last = last

person = Man('asib', 'ahmed')

with open('man.json', 'w') as file:
    p = jsonpickle.encode(person)
    file.write(p)