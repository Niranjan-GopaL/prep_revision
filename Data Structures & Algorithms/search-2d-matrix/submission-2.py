class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        h=m*n-1
        while l<=h:
            mid=l+(h-l)//2
            row_id = mid//n
            col_id = mid%n
            if matrix[row_id][col_id]==target:
                return True
            elif target > matrix[row_id][col_id]:
                l=mid+1
            else:
                h=mid-1
        return False

