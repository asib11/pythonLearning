import pdb ;pdb.set_trace()
list1 = [[1,2],[3,4]]
list2 = [[11,22],[33,44]]
#ok = zip(list1,list2)
#print(list(ok))
#for i in list1:
#    for j in i:
#        print(j)

#for k in list2:
#    for l in k:
#        print(l)

#print([(j,l)])
#result = [(x, y) for x, y in zip(list1, list2)]
#output =list(tuple(zip(i, j)) for i, j in zip(list1, list2))
#print(output)
#print(result)

'''Here are 2 list below
```
list1 = [[1,2],[3,4]]
list2 = [[11,22],[33,44]]
```
I tried to this
```
output =list(tuple(zip(i, j)) for i, j in zip(list1, list2))
```
But my output is not as desired.
```
[((1, 11), (2, 22)), ((3, 33), (4, 44))]
```
I want to one to one correspondence such as output like
```
[(1,11),(2,22),(3,33),(4,44)] 
```
how can I fix this? only zip function can use'''

list3 = [z for i, j in zip(list1, list2) for z in zip(i, j)]
print(list3)
