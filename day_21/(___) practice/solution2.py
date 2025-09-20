class Solution:
    def stringPattern(self, s1: str, s2: str) -> int:
        """
        s1: only contains symbols 0 and 1
        s2: only contains lowercase letters

        task: calculate the number of substrings of s1 that match s2

        conditions:
        1. s1 and s2 are equal length
        2. where there is a 0 in s1, there is a vowel in s2
        3. where there is a 1 in s2, there is a consonant in s2
        """
        vowels = ["a", "e", "i", "o", "u", "y"]

        def check(s1: str, s2: str, index: int) -> int:
            for i in range(len(s1)):
                if s1[i] == "0":
                    if s2[index + i] not in vowels:
                        return 0
                elif s1[i] == "1":
                    if s2[index + i] in vowels:
                        return 0
                    
            return 1
        
        total = 0
        for i in range(len(s2) - len(s1) + 1):
            total += check(s1, s2, i)
        
        return total
    
c = Solution()
s1 = "100"
s2 = "codesignal"
print(c.stringPattern(s1, s2))

s3 = "010"
s4 = "amazing"
print(c.stringPattern(s3, s4))