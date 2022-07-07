item = [1,2,4,5]
item.append(7)
# item.append(7,8) we can't add two or more item in one time
print(item)

item2 = ['asib','malshort', 'dada']
item2.extend(['jabale','akash'])
print(item2)

item.insert(len(item), 'asif') #this also add a item in last
print(item)

item2.insert(1,'rasel')
print(item2)