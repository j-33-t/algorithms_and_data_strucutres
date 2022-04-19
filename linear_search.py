def linear_search(list, target):
    """
    Retruns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    
    return None


# Sorted List

l = [1,2,3,4,5,6,7,8,9,10]
t = 3
linear_search(list = l,target=t)