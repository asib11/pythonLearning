item = {"name": "asib", "address": "kustia", "home": "mongol baria"}

item2 = {key: value.upper() + " OKEY" for key, value in item.items()}
print(item2)
string1 = "abc"
string2 = "123"
item3 = {string1[i]: string2[i] for i in range(len(string1))}
print(item3)

even_odd = range(1, 10)
result = {num: "even" if num / 2 == 0 else "odd" for num in even_odd}
print(result)

item4 = {k.upper() if k == "name" else k: v for k, v in item.items()}
print(item4)

item5 = {k.upper(): v for k, v in item.items() if k == "name"}  #
print(item5)
