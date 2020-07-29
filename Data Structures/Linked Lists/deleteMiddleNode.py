"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) 
of a singly linked list, given only access to that node.
"""

def deleteMiddleNode(node):
    """
    Since we do not have access to the head, the simplest way is to copy the data of next node to the node we want to delete, and then delete the next node.
    Time complexity: O(1)
    Space complexity: O(1)
    """
    if node == None or node.next == None:
        return False
    node.val = node.next.val
    node.next = node.next.next
    return True
