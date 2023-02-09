import time

gen_start = time.time()
print(sum(i for i in range(10000000)))
gen_time = time.time() - gen_start
print( f'gen took {gen_time} time')

list_start = time.time()
print(sum([i for i in range(10000000)]))
list_time = time.time() - list_start
print( f'gen took {list_time} time')