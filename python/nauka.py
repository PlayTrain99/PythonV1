import time

def function_performace(func, how_many_times = 1, **arg):
    print(arg)
    sum = 0

    for i in range(0, how_many_times):
        start  =time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

setContainer = { i for i in range(1000)}
listContainer = [i for i in range(1000)]

def is_elemnt_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False
    
print(function_performace(is_elemnt_in, 5000, what_value=500, container=setContainer))