item = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("item is " + item[2][1])

for x in item:
    for y in x:
        print(y)

# list comprehention

item2 = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
output = [[print(j) for j in i] for i in item2]

bot = [["x" if val % 2 == 0 else "o" for val in range(1, 4)] for ival in range(1, 4)]
print(bot)

numbers = [[num for num in range(1, 5)] for value in range(1, 5)]
print(numbers)
