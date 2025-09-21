from typing import List
from collections import deque

class Solution:
    def shuffleDeck(self, deck: List[int]) -> int:
        """
        Repeatedly move the top card to the bottom until the deck is sorted in ascending order,
        return the number of moves it takes, or return -1 if it is not possible
        """
        n = len(deck)
        target = list(range(1, n + 1))
        if deck == target: return 0
        if sorted(deck) != target: return -1

        queue = deque(deck)
        moves = 0

        while True:
            queue.append(queue.popleft())
            moves += 1
            if list(queue) == target:
                return moves
            if moves > n:
                return -1 
    
c = Solution()
print(c.shuffleDeck([3, 4, 5, 1, 2]))