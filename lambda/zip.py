name = ["asib", "hamza", "tanveer"]
mid = [27, 21, 24]
final = [35, 30, 32]
out_of_30 = [27, 24, 23]

print(dict(zip(name, map(lambda s: s[0] + s[1] + s[2], zip(mid, final, out_of_30)))))
print({t[0]: t[1] + t[2] + t[3] for t in zip(name, mid, final, out_of_30)})
