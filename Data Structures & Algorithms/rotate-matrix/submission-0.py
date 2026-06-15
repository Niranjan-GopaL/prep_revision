class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # in each iteration, we do a huricanne swap ( clockwise swap )
        
        if len(matrix)==1: return 
        n=len(matrix)
        for level in range(n//2):
            # we go from 0 to n-1 if level=0      
            # we go from 1 to (n-1)-1 if level=1
            # we go from 2 to (n-1)-2 if level=2
            # we go from 3 to (n-1)-3 if level=3      
            for j in range(level , n-level-1):
                # hurrican swap
                temp                     = matrix[level][j]
                matrix[level][j]         = matrix[n-j-1][level]
                matrix[n-j-1][level]     = matrix[n-level-1][n-j-1]
                matrix[n-level-1][n-j-1] = matrix[j][n-level-1]
                matrix[j][n-level-1]     = temp




        