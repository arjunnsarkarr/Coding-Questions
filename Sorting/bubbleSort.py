def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
            # print(i," ",arr)
    
    return arr

a = [225,2,49,963,7,61,7,3,5,6,44,98]

print(bubble_sort(a))

