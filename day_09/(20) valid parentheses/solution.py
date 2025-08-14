class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {")": "(", "}": "{", "]": "["}
        stack  = []

        for char in s:
            if char in parentheses.values(): # opening brackets
                stack.append(char)
            elif char in parentheses: # closing brackets
                if not stack or stack[-1] != parentheses[char]:
                    return False
                stack.pop()

        return len(stack) == 0