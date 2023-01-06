name = ["asib", "ahmed", "topu", "opu", "akash"]
name_filter = list(
    map(
        lambda name: f"all name's start with a is {name} ",
        filter(lambda x: x[0] == "a", name),
    )
)
print(name_filter)
