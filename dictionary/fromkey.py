item = {'name':'asib', 'id':31, 'section':2,'intake':40}
item2 = item.copy()
print(f"item2 is {item2}")

fromkey_make = {}.fromkeys(['name','id','intake'],'none')
print(fromkey_make)
fromkey_make2 = dict().fromkeys('abcd','unknown') #if can not use list, each of letter is iterable
print(fromkey_make2)