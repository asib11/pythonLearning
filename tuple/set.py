one_set = {1,2,3,4,5,4,3,2,1,'asib',2.987}
print(list(set(one_set)))  #list->set->list

two_set = {'asib', 'hamza','badhon','tanveer','opi','asib'}
print(f'unique output: {two_set}')  #set give output unique

two_set.add('ahmed')  #add item
print(f'add:{two_set}')

two_set.remove('badhon')
print(f'remove:{two_set}') #remove item

two_set.discard('ahmed') #if you want to remove somthing but you do not want get some error
print(f'discard set 1:{two_set}')

two_set.discard('opi')
print(f'discard set 2:{two_set}')

three_set = two_set.copy()
print(f'copy set: {two_set}')

for i in one_set:
    print(i)

four_set = {'asib','hamza','uthso','abir'}

print(two_set | four_set) #union
print(two_set & four_set) #intersection