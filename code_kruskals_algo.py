def find(parent , x):
    if(parent[x]!=x):
        return find(parent , parent[x])
    return x
def kruskal(grpah):
    #edges
    edges = []

    for u in graph:
        for v , w in graph[u]:
            if(v , u , w) not in edges:
                edges.append((u , v  ,w))
    #sort Edges
    edges.sort(key = lambda x : x[2])
    #parent
    parent = {}
    for node in graph:
        parent[node] = node
    
    #total Cost
    total_cost = 0 
    #traverse Edges
    for (u , v, w) in edges:
        root_u = find(parent , u)
        root_v = find(parent , v)
        if root_u != root_v:
            print(u , "-" , v , ':' , w)
            total_cost += w
            parent[root_v] = root_u

    print("\nMinimum Cost :- " , total_cost)




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

kruskal(graph)