class NameCount:
    def __init__(self, corrent, finish):
        self.corrent = corrent
        self.finish = finish
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.corrent < self.finish:
             i = self.corrent
             self.corrent += 1
             return i
        raise StopIteration

for x in NameCount(1, 5):
    print(x)