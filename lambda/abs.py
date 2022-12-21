item = [10,23,24,35,-99]
print(abs(item[-1]))
print(sum(item))
print(round(abs(sum(item))/2,2))

#zip
item2 = [1,2,3,4,5]
zip_items= list(zip(item,item2))
print(zip_items)
print(list(zip(*zip_items))) #unzip
