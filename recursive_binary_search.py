def recursive_binary_search(list,target):
    """
    Returns the trule value of the target if found, else returns None
    """
    if len(list) == 0:
        return (f"Target found: {False}")
    else:
        midpoint = (len(list)) // 2
        
        if list[midpoint] == target:
            return (f"Target found: {True}")
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target) 
            

l = [1,2,3,4,5,6,7,8,9,10]
t = 2
recursive_binary_search(l,t)