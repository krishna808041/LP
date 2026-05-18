import heapq
graph = {
    'A' : [('B' , 1) , ('C' , 4)],
    'B':[('D' , 2) , ('E'  , 5)],
    'C':[('E' , 1)],
    'D':[('G' , 3)],
    'E':[('G' , 2)],
    'G':[]
}
heuristics = {
    'A' : 6 ,
    'B' : 4 ,
    'C' : 2 ,
    'D' : 3 ,
    'E' : 1 , 
    'G' : 0 
}
def a_star(start , goal):
    open_list = []
    heapq.heappush(open_list , (heuristics[start] , 0 , start , [start]))
    visited = set()
    while open_list:
        f , g , current , path = heapq.heappop(open_list)
        if(current ==goal):
            print("Goal Founded!")
            print("Path : ", path)
            print("Cost :-" , g)
            return
        
        visited.add(current)

        for neigbhour , cost in graph[current]:
            if neigbhour not in visited:
                g_new = g+cost
                f_new = g_new + heuristics[neigbhour]
                heapq.heappush(open_list , (f_new , g_new , neigbhour , path + [neigbhour]))
    print("Goal Not Found")            

a_star('A' , 'G')