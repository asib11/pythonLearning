nums = ['banana','apple','orange']
index = 0
while index < len(nums) :
    print(f"{index+1}:{nums[index]}")
    index += 1

cars = ['audi','ford','tesla']

for i,x in enumerate (cars, start=1) :
    print(f"{i}:{x}")