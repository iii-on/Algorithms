from random import randint

def random_list(count, max_number):
    list = []
    for i in range(0, count):
        list.append(randint(1, max_number))
    list.sort()
    return list

def binary_search(list, item):

    low = 0
    high = len(list) - 1

    while low <= high:
      
        middle = (low + high) // 2
       
        if list[middle] == item:
            return middle
        elif list[middle] > item:
            high = middle - 1
        else:
            low = middle + 1

    return False


if __name__=="__main__":
    list = random_list(10, 40)
    print(f"Binary search 23 in List->{list}")
    print(f"Position = {binary_search(list, 23)}")
