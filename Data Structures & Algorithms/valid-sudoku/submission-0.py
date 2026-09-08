class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [set() for x in range(9)]
        column = [set() for x in range(9)]
        box = [set() for x in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)

                if value in row[r] or value in column[c] or value in box[box_index]:
                    return False
                
                row[r].add(value)
                column[c].add(value)
                box[box_index].add(value)
        return True