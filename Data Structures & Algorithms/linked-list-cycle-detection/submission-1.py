# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        
        slowNode = head
        fastNode = head.next

        while slowNode.next != None and fastNode.next and fastNode.next.next != None:
            # if cycle then the fast node will eventually end up on same node as slow
            slowNode = slowNode.next
            fastNode = fastNode.next.next

            if (slowNode == fastNode):
                return True

        return False
