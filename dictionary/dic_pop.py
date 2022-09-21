item = {'name': 'asib','id':3031,'intake':40,'email':'asib@gmail.com'}
update_item ={'section':2}
print(item.pop('email')) #or del item['email']
item.update(update_item)
print(item)
print(item.popitem())
