class DicPlay(dict):
    def __repr__(self) -> str:
        return super().__repr__()

    def __missing__(self, key):
        return f'this {key} is not here'
    
    def __setitem__(self,key,value) :
        print('ok now i update')
        return super().__setitem__(key, value)


data =DicPlay({'first':'asib', 'last': 'ahmed'})
print(data)
print( data['set'])
# print(data)
data['age'] = 20
print(data)
