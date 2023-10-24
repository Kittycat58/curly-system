def linear_search(array,target):
    for i in array:
        if i == target:
            return array.index(i)
    return -1

# test run 
a = [1,2,3,4,5,6]
print(linear_search(a,2))
print(linear_search(a,10))
    
    