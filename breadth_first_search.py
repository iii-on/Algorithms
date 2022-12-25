from collections import deque


def person_search(person):
    if person[0:1] == "K":
        return True
    return False
    
def breadth_first_search(name):
    search_graph = deque()
    search_graph += graph[name]
    searched = []
    while search_graph:
        person = search_graph.popleft()
        if not person in searched and person_search(person):
            print("Start with letter ->", person)
            return True
        else:
            if person in graph:
                search_graph += graph[person]
                searched.append(person)
    return False
            

graph = {}
graph["You"] = ["Alex", "Fill", "John"]
graph["Alex"] = ["Eric", "Kate"]
graph["John"] = ["Kurt", "Tom"]

breadth_first_search("You")