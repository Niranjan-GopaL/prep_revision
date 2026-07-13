class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # row,col,boxes=[[0]*9]*9, [[0]*9]*9, [[0]*9]*9
        row,col,boxes=[[0]*9 for _ in range(9)], [[0]*9 for _ in range(9)], [[0]*9 for _ in range(9)]

        box = lambda r,c : (r//3)*3+(c//3)
        need=[]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    need.append((r,c))
                else:
                    v=board[r][c]
                    row[r][int(v)-1]=1
                    col[c][int(v)-1]=1
                    boxes[box(r,c)][int(v)-1]=1
        
        def bt(i):
            if i==len(need): return True
            r,c=need[i]
            for d in [1,2,3,4,5,6,7,8,9]:
                if row[r][d-1] or col[c][d-1] or boxes[box(r,c)][d-1]:
                    continue
                row[r][d-1]=1; col[c][d-1]=1; boxes[box(r,c)][d-1]=1
                board[r][c]=str(d)
                if bt(i+1):
                    return True
                board[r][c]=""
                row[r][d-1]=0; col[c][d-1]=0; boxes[box(r,c)][d-1]=0
            return False
        bt(0)