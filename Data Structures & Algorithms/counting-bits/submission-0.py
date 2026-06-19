class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1) :
            cnt=0
            for k in range(10):
                cnt += 1 if ((i>>k)&1)==1 else 0
            ans.append(cnt)
        return ans
