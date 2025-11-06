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

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow
    
def create_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

c = Solution()

print(c.findDuplicate([1,3,4,2,2]))
print(c.findDuplicate([3,1,3,4,2]))
print(c.findDuplicate([2,2,2,2,2]))