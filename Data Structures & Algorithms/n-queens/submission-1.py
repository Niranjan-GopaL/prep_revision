class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        a = [ ['.']*n for _ in range(n)]
        attacked = [ [0]*n   for _ in range(n)]
        ans = []

        def valid(i,j):
            return ( i<0 or j<0 or i>=n or j>=n ) == False


        def add(i,j,mark):
            for ki in range(n): # the entire col is marked
                attacked[ki][j]+=1 if mark else -1
            for kj in range(n): # the entire row is marked
                attacked[i][kj]+=1 if mark else -1

            # Blocking diagonals is the hardest
            # This is such a beautiful code

            # top left to bottom right diagonal
            ki=i
            kj=j
            while valid(ki,kj):
                attacked[ki][kj]+=1 if mark else -1
                ki-=1
                kj-=1
            ki=i
            kj=j
            while valid(ki,kj):
                attacked[ki][kj]+=1 if mark else -1
                ki+=1
                kj+=1

            # top right to bottom left diagonal
            ki=i
            kj=j
            while valid(ki,kj):
                attacked[ki][kj]+=1 if mark else -1
                ki-=1
                kj+=1
            ki=i
            kj=j
            while valid(ki,kj):
                attacked[ki][kj]+=1 if mark else -1
                ki+=1
                kj-=1

        hash_set = set()
        def f(i, remaining):
            if remaining==0:
                curr = tuple([''.join(arr) for arr in a ])
                if curr not in hash_set:
                    ans.append(list(curr))
                    hash_set.add(curr)
                return

            for j in range(n):
                if attacked[i][j] == 0 :
                    # pick Queen here
                    add(i,j,0)
                    a[i][j]='Q'
                    remaining-=1
                    f(i+1, remaining)

                    # unpick Queen here
                    a[i][j]='.'
                    add(i,j,1)
                    remaining+=1
                    # f(remaining)
        
        f(0, n)
        return ans