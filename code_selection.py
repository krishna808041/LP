def selection_Sort(arr):
    n= len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1 , n):
            if(arr[j]<arr[min_index]):
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] ,arr[i]
    return arr

arr = [81 , 75 , 45 , 12 , 10]
print("Selection Sorting ",selection_Sort(arr))