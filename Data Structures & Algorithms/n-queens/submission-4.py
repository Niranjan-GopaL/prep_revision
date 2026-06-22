class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        a = [['.'] * n for _ in range(n)]
        # how many queens hit this cell :
        attacked = [[0] * n for _ in range(n)]   
        ans = []

        def valid(i, j):
            return 0 <= i < n and 0 <= j < n

        def mark(i, j, delta):
            for k in range(n):
                attacked[i][k] += delta          # row
                attacked[k][j] += delta          # column
            for di, dj in ((-1,-1), (1,1), (-1,1), (1,-1)):
                ki, kj = i + di, j + dj
                while valid(ki, kj):
                    attacked[ki][kj] += delta
                    ki += di; kj += dj

        def f(row):
            if row == n:
                ans.append([''.join(r) for r in a])
                return

            for c in range(n): # THE LOOP ITSELF DEOS THE "unpick" by moving next to next pick
                if attacked[row][c] == 0:
                    mark(row, c, +1); a[row][c] = 'Q' # pick
                    f(row + 1)
                    a[row][c] = '.'; mark(row, c, -1)

        f(0)
        return ans