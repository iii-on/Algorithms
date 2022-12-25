from random import randint

def random_list():
    list = []
    for i in range(0,10):
        list.append(randint(0,10))
    return list

def summa_of_list(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + summa_of_list(list, size - 1)
        
        
list = random_list()
print("List-> ", list)
print("Summa of list = ", summa_of_list(list, 10))