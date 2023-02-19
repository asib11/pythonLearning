import pickle


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"my name is {self.name} and age is {self.age}"


class Student(Person):
    def __init__(self, name, age, id, intake):
        super().__init__(name, age)
        self.id = id
        self.intake = intake

    def student_info(self):
        return f"student id is {self.id} and intake is {self.intake}"


asib = Student("asib", 24, 31, 40)
# print(asib)
# print(asib.student_info())

with open("data.pickle", "wb") as file:
    pickle.dump(asib, file)
