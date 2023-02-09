def fbinacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1
        
for i in fbinacci(10):
    print(i)