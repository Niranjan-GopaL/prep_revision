class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans,path=[],[]
        candidates.sort()
        n=len(candidates)
        def f(start,remain):
            if remain==0:
                ans.append(path[:])
                return
            for i in range(start, n):
                if candidates[i]>remain:
                    break
                if i>start and (candidates[i]==candidates[i-1]):
                    continue
                path.append(candidates[i])
                f(i+1,remain-candidates[i])
                path.pop()
        f(0,target)
        return ans