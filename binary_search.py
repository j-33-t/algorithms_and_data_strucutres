def binary_search(list,target):
    """
    Retruns the index position of the target if found, else returns None
    """
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first+last) // 2
        
        if list[midpoint] == target:
            return (f"index of target is {midpoint}")
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

# Sorted List

l = [1,2,3,4,5,6,7,8,9,10]
t = 8
binary_search(l,t)