jobs = [
    ('J1' , 2 , 100),
    ('J2' , 1 , 50) , 
    ('J3' , 2 , 10) ,
    ('J4' , 1 , 20)
]

jobs.sort(key = lambda x :x[2] , reverse = True)
profit = 0
result = []
slots = [False]*3
for job in jobs:
    for i in range(job[1]-1 , -1 , -1):
        if(slots[i]==False):
            slots[i] = True
            result.append(job[0])
            profit += job[2]
            break

print(result)
print(profit)