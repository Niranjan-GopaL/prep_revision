class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # lower_bound on which row
        m,n=len(matrix),len(matrix[0])

        l=0
        h=m-1
        start=0
        while l<=h:
            mid=l+(h-l)//2
            if matrix[mid][n-1]==target:
                return True
            elif matrix[mid][n-1] > target:
                start=mid
                h=mid-1
            else:
                l=mid+1
        
        # search from 'start onwards

        def search(i, matrix, target):
            l=0
            h=n-1
            while l<=h:
                mid=l+(h-l)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid] > target:
                    h=mid-1
                else:
                    l=mid+1
            return False

        for i in range(start,m):
            if search(i,matrix,target):
                return True
        return False

