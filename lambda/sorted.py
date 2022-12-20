sorted_list = [{'username': 'asib','id' : 1, 'program': 'CSE', 'courses':['math','python','oop']},{'username': 'ahmed','id' : 2, 'program': 'CSE', 'courses':['english']},{'username': 'prema','id' : 3, 'program': 'CSE', 'courses':[]},{'username': 'tanveer','id' : 4, 'program': 'CSE', 'courses':['physics','c++']}]

#ok = sorted(sorted_list,key = lambda u : len(u['courses']))
#print(ok)

print(sorted(sorted_list,key = lambda u : len(u['courses']))[1])