

def sort_algo(arr):
    temp = 0
    for i in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp

    print(arr)


sort_algo([9,8,7,5,2,4,5,6,1])
            
        

