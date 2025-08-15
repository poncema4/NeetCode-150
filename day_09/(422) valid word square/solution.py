class Solution:
    def validWordSquare(self, words):
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True
    
if __name__ == "__main__":
    words1 = ["ball", "area", "read", "lady"]
    c = Solution()
    assert c.validWordSquare(words1) == False

    words2 = ["abcd", "bnrt", "crmy", "dtye"]
    assert c.validWordSquare(words2) == True