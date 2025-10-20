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
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of the linked list
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

def create_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

c = Solution()

l = create_linked_list([1, 2, 3, 4, 5])
print("Before reorder:", l)
c.reorderList(l)
print("After reorder:", l)

l2 = create_linked_list([2, 4, 6, 8])
print("Before reorder:", l2)
c.reorderList(l2)
print("After reorder:", l2)