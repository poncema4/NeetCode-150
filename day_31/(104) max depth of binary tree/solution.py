from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
def printTree(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

c = Solution()
root = TreeNode(3)
root.left = TreeNode(9, None, None)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(c.maxDepth(root))