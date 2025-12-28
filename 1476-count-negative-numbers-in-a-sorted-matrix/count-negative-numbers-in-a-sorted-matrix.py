class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        count = 0
        
        for row in grid:
            for j in range(columns):
                if row[j] < 0:
                    count += columns - j
                    break 
        return count