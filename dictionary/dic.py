import pdb

pdb.set_trace()
first_dic = {"name": "asib", "age": 24, "study lavel": "bsc engg"}
print(first_dic)
print(f"one of the dic value {first_dic['name']}")
for key, value in first_dic.items():
    print(f"key is {key} and value is {value}")

for v in first_dic.values():
    print(v)

for item in first_dic.items():
    print(item)

# using dictionary
name = "name" in first_dic
print(name)

email = "email" in first_dic
print(email)

value = "asib" in first_dic.values()
print(value)

second_dic = dict(name="ahmed", home="kushtia")  # other type of define dictionary
print(second_dic)
print(second_dic.clear())
second_dic["name"] = "asib"
second_dic["phone"] = 8801753249719
print(second_dic)
