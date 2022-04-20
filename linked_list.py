from this import d


class Node:
    """
    An Object for Storing a single node of a linked List:
    Models two attribtues - data and the link to the next node in the list
    """
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "< Node data: %s >" % self.data
    
    
class LinkedList: 
    """
    Singly Linked List
    """
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None