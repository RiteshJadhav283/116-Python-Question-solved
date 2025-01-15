import time

start_time=time.time()

list_comprehension=[x*2 for x in range(1000000)]
list_comprehension_time=time.time()-start_time
start_time=time.time()

generator_expression=(x*2 for x in range(1000000))
generator_expression_time=time.time()-start_time

print("List comprehension time:",list_comprehension_time)
print("Generator expression time:",generator_expression_time)