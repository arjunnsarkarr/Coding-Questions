def twoSum(arr,sumOfTwo):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sumOfTwo :
                return [arr[i],arr[j]]

arrr= [2,15,4,3,1,62,4]
target = 63




print(twoSum(arrr,target))





