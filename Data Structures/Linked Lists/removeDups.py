"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP -> How would you solve this problem if a temporary buffer is not allowed?
"""

class Node:
    """
    A simple class for a linked list node.
    """
    def __init__(self, val):
        self.val = val
        self.next = None
        
def createList(elements):
    """
    Function to create a linked list with values supplied as a list.
    Returns the head of the linked list.
    """
    head = Node(elements[0])
    current = head
    for i in elements[1:]:
        current.next = Node(i)
        current = current.next
    return head

def traverseList(head):
    """
    Prints the linked list starting from the head
    """
    while head:
        print(head.val)
        head = head.next

        
def removeDups(head):
    """
    To track duplicates, a simple hash set can be used.
    We simply iterate through the linked list, adding each element to the set. When a duplicate element is encountered, we can simply remove it, 
    and continue iterating till the end of the list.
    Time complexity: O(n)
    Space complexity: O(n)
    where n is the number of nodes in the list.
    """
    elements = set()
    previous = head
    current = head.next
    elements.add(previous.val)
    while current:
        if current.val in elements:
            previous.next = current.next
        else:
            elements.add(current.val)
            previous = current
        current = current.next
        
def removeDups2(head):
    """
    If buffer is not allowed, we can use two pointers: one to iterate through the linked list, and the other to iterate through all subsequent items.
    If the second pointer comes across an item which has the same value as that of the first pointer, we simply remove it.
    Time complexity: O(n^2)
    Space complexity: O(1)
    where n is the number of nodes in the list.
    """
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next   
        

#Testing...

head = createList([1,2,2,1,4])
traverseList(head)
removeDups2(head) #or removeDups2(head)
traverseList(head)
