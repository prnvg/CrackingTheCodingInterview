"""
Return Kth to Last: Implement an algoritthm to find the kth to last element of a singly linked list.
"""

def createList(elements):
    """
    Function to create a linked list with values supplied as an ArrayList.
    Returns the head of the linked list.
    """
    head = Node(elements[0])
    current = head
    for i in elements[1:]:
        current.next = Node(i)
        current = current.next
    return head

def returnKthToLast(head, k):
    """
    Uses two pointers, sets them k elements apart. Then moves both the pointers till one reaches the end of the list. At this time, 
    return the value at the other pointer.
    """
    counter = 1
    current = head
    last = head
    
    while(counter < k):
        last = last.next
        if last == None:
            return None
        counter += 1
        
    while(last.next):
        last = last.next
        current = current.next
        
    return current.val
    
#Testing...
head = createList([1,2,2,1,4,2,3,4,5,6])
returnKthToLast(head, 3)
