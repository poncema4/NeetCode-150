# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        l = dummy
        r = head 

        while n > 0 and r:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next

        # delete the node
        l.next = l.next.next

        return dummy.next
    
def create_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

c = Solution()

head = create_linked_list([1, 2, 3, 4, 5])
n = 2
print(c.removeNthFromEnd(head, n))

head2 = create_linked_list([0, 1])
n2 = 1
print(c.removeNthFromEnd(head2, n2))