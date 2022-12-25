from random import randint


def random_array():
    array=[]
    for i in range(0,10):
        array.append(randint(0,10))
    return array
    
def search_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest
    
def select_sort(array):
    sort_array = []
    for i in range(len(array)):
        smallest_item = search_smallest(array)
        sort_array.append(smallest_item)
        array.remove(smallest_item)
    return sort_array
    
    
random_array = random_array()
print(random_array)
print(select_sort(random_array))