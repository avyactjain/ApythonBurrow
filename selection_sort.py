def swap(x, y):
    return y, x


def find_minimum(arr):
    min = arr[ 0 ]
    for a in arr:
        if a < min:
            min = a
    return min
    
    
arr = [64,25,12,22,11]



for i in range(0,5):
    x = find_minimum(arr[i:5])
    index_x = arr.index(x)
    arr[i],arr[index_x] = arr[index_x],arr[i]
    
    

print(arr)    
