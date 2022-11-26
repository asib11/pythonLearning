from collections import Counter
num_of_shoe = int(input())
my_list =list(map(int,input().split()))
print(my_list)
quantity = Counter(my_list)
total = 0
num_of_buy = int(input())
for i in range(num_of_buy): 
    size, price = map(int,input().split())
    if quantity[size]>0:
        total += price
        quantity[size] -= 1

print(total)


