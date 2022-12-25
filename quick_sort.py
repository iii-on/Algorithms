from random import randint

def random_list(n):
    list = []
    for i in range(0,n):
        list.append(randint(0,10))
    return list
    
def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
        
        
random_list = random_list(10)
print("List-> ", random_list)
print("Quick sorted list -> ", quick_sort(random_list))