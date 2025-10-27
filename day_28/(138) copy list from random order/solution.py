# Definition for singly-linked list with random pointer.
class ListNode(object):
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        result = []
        curr = self
        while curr:
            rand_val = curr.random.val if curr.random else None
            result.append(f"[{curr.val},{rand_val}]")
            curr = curr.next
        return " -> ".join(result)

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = {None: None}
        curr = head

        while curr:
            copy = ListNode(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]

def create_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

c = Solution()

head = create_linked_list([3, 7, 4, 5])
head.random = None
head.next.random = head
head.next.next.random = head
head.next.next.next.random = head.next

print("Input: ", head)
copied_head = c.copyRandomList(head)
print("Output:", copied_head)

head2 = create_linked_list([1, 2, 3])
head2.random = head2.next.next
head2.next.random = head2
head2.next.next.random = head2.next

print("\nInput: ", head2)
copied_head2 = c.copyRandomList(head2)
print("Output:", copied_head2)