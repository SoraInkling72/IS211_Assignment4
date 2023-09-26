import random
import time
st = time.time(sequential_search)

def get_me_random_list(n):
    n = range(1-1000)
    for i in range(1, 500):
        y = random.randrange(500)
    return list(range(500))

    a_list = list(range(500))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
    else:
        pos = pos + 1
    return found

multiple_lists = (100*a_list[500])

print(sequential_search(multiple_lists))

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(sequential_search)

elapsed_time = et - st
print('Sequential Search took', elapsed_time, 'seconds to run, on average')

st = time.time(sequential_search)
def ordered_sequential_search(a_list):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
        else:
            pos = pos + 1
    return found

multiple_lists = (100*a_list[500])

print(ordered_sequential_search(multiple_lists))

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(ordered_sequential_search)

elapsed_time = et - st
print('Ordered Sequential Search took', elapsed_time, 'seconds to run, on average')

st = time.time(sequential_search)
def binary_search_iterative(a_list):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
        else:
            first = midpoint + 1
    return found

multiple_lists = (100*a_list[500])

print(binary_search_iterative(multiple_lists))

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(binary_search_iterative)

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


st = time.time(sequential_search)
def binary_search_recursive(a_list):
    if len(a_list) == 0:
        return False
else:
    midpoint = len(a_list) // 2
if a_list[midpoint] == item:
    return True
else:
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1:], item)

multiple_lists = (100*a_list[500])

print(binary_search_recursive(multiple_lists))

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(binary_search_recursive)

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

if __name__ == "__main__":
    """Main entry point"""
    the_size = 500

    total_time = 0
    for i in range(500):
        mylist = get_me_random_list(the_size)
        # sorting is not needed for sequential search.
        mylist = sorted(mylist)

        start = time.time()
        check = binary_search_iterative(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")