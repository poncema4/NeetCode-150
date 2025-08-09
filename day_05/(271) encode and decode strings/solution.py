from collections import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # ["marco"] -> "5#marco"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # j pointer is in charge of finding the delimiter #
        # i pointer is in charge of finding the beginning of the next string

        while i < len(s):
            j = i
            while s[j] != "#": # guaranteed to be found based on our format
                j += 1
            length = int(s[i:j]) # how many following characters after j to get all the correct chars
            # j is the delimeter = # so j + 1 is the first character in the string
            # the end of the string j + 1 + length will give the entire string
            res.append(s[j+1:j+1+length])
            # pointer i will be the beginning of the next string or the end of the entire string
            i = j + 1 + length
        
        return res

# Difficulty: Medium