import random
import time
st = time.time(sequential_search)

def get_me_random_list(n):
    n = range(1 - 1000)
    for i in range(1, 500):
        y = random.randrange(500)
    return list(range(500))

    a_list = list(range(500))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

multiple_lists = (100*a_list[500])

print(insertion_sort(multiple_lists))

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(insertion_sort)

elapsed_time = et - st
print('Insertion Sort took', elapsed_time, 'seconds to run, on average')

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
        while sublist_count > 0:
            for start_position in range(sublist_count):
                gap_insertion_sort(a_list, start_position, sublist_count)
            print("After increments of size", sublist_count, "The list is", a_list)

    sublist_count = sublist_count // 2

multiple_lists = (100*a_list[500])

print(shell_sort(multiple_lists))

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(shell_sort)

elapsed_time = et - st
print('Shell Sort took', elapsed_time, 'seconds to run, on average')

def gapInsertionSort(a_list, start, gap):

    for i in range(start+gap, len(a_list), gap):
        currentvalue = a_list[i]
        position = i

        while position >= gap and a_list[position-gap] > currentvalue:
            a_list[position] = a_list[position-gap]
            position = position - gap

        a_list[position] = currentvalue

multiple_lists = (100*a_list[500])

print(gapInsertionSort(multiple_lists))

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(gapInsertionSort)

elapsed_time = et - st
print('Gap Insertion Sort took', elapsed_time, 'seconds to run, on average')

def python_sort(a_list):
    sorted(a_list)= shell_sort(a_list).sort
    return sorted(a_list)

sum_x = 0
for i in range(1000000):
    sum_x += i

et = time.time(python_sort)

elapsed_time = et - st
print('Python Sort took', elapsed_time, 'seconds to run, on average')


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    # the_size = list_sizes[0]

    for the_size in list_sizes:
        total_time = 0
        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            sorted_list = python_sort(mylist500)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"Python sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        total_time = 0
        for i in range(100):
            mylist500 = get_me_random_list(the_size)
            start = time.time()
            insertion_sort(mylist500)
            time_spent = time.time() - start
            total_time += time_spent

        # Repeat the same loop and use shellSort(...)

        avg_time = total_time / 100
        print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")