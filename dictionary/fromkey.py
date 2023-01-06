item = {"name": "asib", "id": 31, "section": 2, "intake": 40}
item2 = item.copy()
print(f"item2 is {item2}")

fromkey_make = {}.fromkeys(["name", "id", "intake"], "none")
print(fromkey_make)
# if can not use list, each of letter is iterable
fromkey_make2 = dict().fromkeys("abcd", "unknown")
print(fromkey_make2)

# if we use get it does not show error if there is no existed key

print(item.get("name"))

if item.get("unversity name") == None:
    print("not found")

print(f"output: {item.clear()}")
