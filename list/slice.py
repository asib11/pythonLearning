item = ['white','blue','green', 'yellow']
print(item[1:]) #start point to forword
print(item[1::-1]) #start point to backword all
print(item[-1::-1]) #start last point to backword all

#item = ['white','blue','green', 'yellow']
print(item[::2])
print(item[1:4:2])
print(item[:1:-1]) #it means last index to end point all element reversing

string = 'my name is asib'
print(string[::-2]) #string revese
item2 = ['white','blue','green', 'yellow']
item2[2:4] =[1,2] #replace the index
print (item2)