import heapq
def prims(graph , start):
    visited = set()
    total_cost = 0
    min_heap = [(0 , start)]
    while min_heap:
        cost , node = heapq.heappop(min_heap)
        if node  in visited:
            continue
        visited.add(node)
        total_cost+=cost 
        print(node , end=" ")
        for neighbour , weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(min_heap , (weight , neighbour))
    
    print("\nMinimum Cost is :- " , total_cost)


graph = {
    "a":[("b",1),("c",6) , ("d" , 5)],
    "b":[("a",1),("c",6) ],
    "c":[("a",6),("b",6) , ("f" , 3), ("e" , 7)],
    "d":[("a",5),("f",2) , ("g" , 10)],
    "e":[("h",12),("c",7) ],
    "f":[("h",8),("c",3) , ("d" , 2)],
    "g":[("h",7),("i",3) , ("d" , 10)],
    "h":[("g",7),("f",8) , ("i" , 8) , ("e" , 12)],
    "i":[("g",3),("h",8) ],
}

prims(graph , "b")

