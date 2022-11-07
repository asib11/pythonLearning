create_list = [{'username': 'asib','id' : 1, 'program': 'CSE', 'courses':['math','python','oop']},{'username': 'ahmed','id' : 2, 'program': 'CSE', 'courses':['english']},{'username': 'prema','id' : 3, 'program': 'CSE', 'courses':[]},{'username': 'tanveer','id' : 4, 'program': 'CSE', 'courses':['physics','c++']}]
print(min(create_list, key = lambda name : name['username'])['id'])

reverse_item = 'I am going to write a research paper'
print(''.join(list(reversed(reverse_item))))

for i in reversed('asib'):
    print(i)