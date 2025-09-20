from typing import List

class Solution:
    def stringPattern(self, field: List[List[int]], figure: List[List[int]]) -> int:
        """
        field: size height x width (only containing 0s and 1s)
        figure: size 3 x 3 (only containing 0s and 1s)

        1 --> the cell is occupied
        0 --> the cell is empty

        task: find the dropping position that at least one full row is formed
        edge: if there are multiple dropping positions return any of them
        else: if there is no such dropping position, return -1
        """
        height = len(field)
        width = len(field[0])
        figure_size = len(figure)

        for col in range(width - figure_size + 1):
            row = 0
            while row <= height - figure_size:
                collision = False
                for i in range(figure_size):
                    for j in range(figure_size):
                        if figure[i][j] == 1 and field[row + j][col + j] == 1:
                            collision = True
                            break
                    if collision:
                        break

                if collision:
                    break
                row += 1

            final_row = row - 1
            if final_row < 0:
                continue

            for i in range(figure_size):
                row_filled = True
                for c in range(width):
                    if not (field[final_row + i][c] == 1 or \
                            (col <= c < col + figure_size and figure[i][c - col] == 1)):
                        row_filled = False
                        break

                if row_filled:
                    return col
                
        return -1
    
c = Solution()
field = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

figure = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
]
print(c.stringPattern(field, figure))