class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans,path=[],[]
        def f(start):
            if len(path)==k: 
                ans.append(path[:])
                return
            need = k-len(path)
            for i in range(start, n-need+1 +1):
                path.append(i)
                f(i+1)
                path.pop()
        f(1)
        return ans