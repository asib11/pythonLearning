students = {}
for item in range(int(input())):
    name = input()
    score = float(input())
    students[name] = score

values1 = list(students.values())
set1 = set(values1)
list1 = sorted(list(set1), reverse=True)
runner = (list1[len(list1) - 2])

runner_students = sorted([k for k,v in students.items() if v == runner])
for item in runner_students:
    print(item)