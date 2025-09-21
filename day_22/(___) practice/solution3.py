from typing import List, Tuple
from collections import defaultdict

class Solution:
    def countSubmatrices(self, rows: int, cols: int, black: List[Tuple[int, int]]) -> List[int]:
        """
        Count the number of 2x2 submatrices with 0, 1, 2, 3, or 4 black cells
        """
        submatrix = defaultdict(int)

        for r, c in black:
            for dr, dc in [(-1, -1), (-1, 0), (0, -1), (0, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows -1 and 0 <= nc < cols - 1:
                        submatrix[(nr, nc)] += 1

        result = [0] * 5
        total_submatrices = (rows - 1) * (cols - 1)

        for count in submatrix.values():
            result[count] += 1

        result[0] = total_submatrices - sum(result[1:])

        return result
    
c = Solution()
print(c.countSubmatrices(4, 5, [(0, 1), (1, 2), (2, 3), (3, 4)]))