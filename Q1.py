def alternate_numbers(arr):
    positive = [num for num in arr if num > 0]
    negative = [num for num in arr if num < 0]
    
    result = []
    while positive and negative:
        result.append(positive.pop(0))
        result.append(negative.pop(0))
    
    result.extend(positive)
    result.extend(negative)
    return result

# Test case
print(alternate_numbers([-3, 1, 2, 4, -6, 8, -8, -1]))          # output: [1, -3, 2, -6, 4, -8, 8, -1]
print(alternate_numbers([-3, 1, 2, 4, -6, 5,8,6, -8, -1]))      # output: [1, -3, 2, -6, 4, -8, 5, -1, 8, 6]
print(alternate_numbers([1, 2, 3]))                             # output: [1, 2, 3]
print(alternate_numbers([-1, -2, -3]))                          # output: [-1, -2, -3]
