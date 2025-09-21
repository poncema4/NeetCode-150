class Solution:
    def countSameWord(self, text: str) -> int:
        """
        Count the number of words that start and end with the same letter (lowercase and uppercase)
        """
        if not text:
            return 0
        
        words = text.split()
        count = 0

        for word in words:
            clean_word = "".join(char for char in word if char.isalpha())

            if len(clean_word) > 0:
                if clean_word[0].lower() == clean_word[-1].lower():
                    count += 1

        return count

c = Solution()
print(c.countSameWord("leveL Upper ranK In infinity caStlEC"))