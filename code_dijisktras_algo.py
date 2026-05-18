import heapq
def dijikstra(graph , start):
    #distamce
    distance = {}
    #mark distace as infinity
    for node in graph:
        distance[node] = float("inf")
    #Mark distance as 0
    distance[start] = 0
    #make min_heap
    min_heap = [(0 , start)]
    #run till min_heap
    while min_heap:
        #use the node from min_heap through pop
        curr_dist , node = heapq.heappop(min_heap)
        #check if that current_dist is >distance[node]
        if curr_dist > distance[node]:
            continue
        #traverse to the neighbour
        for neighbour , cost in graph[node]:
            #make the new_dist
            new_dist = curr_dist + cost
            #check if the new_dist <distance[neighbour] then update the distance[neigbour]
            if new_dist < distance[neighbour] :
                distance[neighbour] = new_dist
                #add the new_dist , neighbour to min_heap
                heapq.heappush(min_heap ,(new_dist , neighbour))

    print("\nDistances of Source to Destination :- ")
    for node in distance:
            print(start,"-",node,":",distance[node])
    


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

dijikstra(graph , "a")