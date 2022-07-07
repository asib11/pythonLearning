item = [1,2,4,5,7,2,3,5,6,76]
print(item.index(2))
print(item.index(2,1)) #start point 1 no index
print(item.index(2,2,6)) #range 2 to 6 index

print(item.count(2)) #count method

item.reverse()
print(item)

item.sort()
print(item)

joined = ['asib','ahmed', '31']
#output =' '.join(joined)
print(' '.join(joined)) #join methon can use only for string
#print(output)
