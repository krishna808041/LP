from collections import deque

graph = {}

def createGraph(graph):
    n = int(input("Enter the Number of Vertices:- "))
    for i in range(n):
        vertex = int(input("Enter The Name of Vertex :- "))
        graph[vertex] = []
    
    e = int(input("Enter The No. of Edges :- "))
    for j in range(e):
        st = int(input("Enter the Sarting Vertex :- "))
        en = int(input("Enter the Ending Vertex :- "))
        graph[st].append(en)
        graph[en].append(st)
    print("The graph Created Successfully")

def displayGraph():
    if not graph:
        print("Graph is Empty!.Create Graph First")
        return
    print("\nAdjacency List ")
    for vertex in graph:
        print(vertex ,"->", graph[vertex])

def bfs(graph , start):
    if start not in graph:
        print("Start Not in Graph . SEE Carefully")
        return

    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("BFS Sequence :- ")

    while queue:
        current = queue.popleft()
        print(current , end=" ")


        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print()

    
def dfs(graph , visited , start):
    if start not in graph:
        print("Start Not in Graph . SEE Carefully")
        return
    visited.add(start)
    print(start , end=" ")
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph , visited , neighbour)


def menu(graph):
    while True:
        print("\n=========Menu===========")
        print("1. Create A Graph")
        print("2. Display a Graph")
        print("3. Show BFS Sequence")
        print("4. Show DFS Sequence")
        print("5. Exit")

        choice = int(input("Enter the Choice Number :"))

        if(choice==1):
            createGraph(graph)
        elif(choice==2):
            displayGraph()

        elif(choice==3):
            start = int(input("Enter the Starting Point:- "))
            bfs(graph , start)

        elif(choice==4):
            start = int(input("Enter the Starting Point:- "))
            dfs(graph , set() , start)
            print()

        elif(choice == 5):
            print("Ending ...")
            return
        else:
            print("Choose the Choice Correctly!")
            

        


        
menu(graph)