# VERSION where I start from 0 : this does got give optimal answer ?
# LIS[i] = LIS ending at i

# for k in range(n): 
#       curr=nums[k]
#       for i in range(k+1,n):
#           if nums[i] > curr:
#               LIS[i]=max(LIS[i], cnt+1)
#               cnt+=1
#               curr=nums[i]


# I think the key is OPTIMAL substrcture 
# or in simple words : WHICH APPROACH DOES LESSER WORK
# going from 0 to up does not gaurentee LIS[i] is correct UNTIL reach i 
# ( by then all possible LIS that ends in i would be covered)
# That is the fundamental difference. The checks here are more fundamentally 
# we can't memoize LIS[i] as we can do if we go from end
# both are O(n2) tho 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # VERSION where we go from end
        # it's useful to maintain a stack as well
        # Wrong version
        # Actually going up and goind down won't give you the exact LIS[i] until you reach i

        # I CONFUSED THIS WITH A GREEDY PROBLEM.
        # This is NOT a greedy problem

        # if nums[i-1]<nums[i]:
        #      LIS[i] = LIS[i-1] + 1


        n=len(nums)
        LIS=[0]*n

        # # WE NEED TO simulate picking all possible "curr" 
        # def dfs(i, curr):
        #     if i==-1:return 0

        #     if nums[i] < curr:
        #         LIS[i] = 1 + max( dfs(i-1, nums[i]))
        #         return LIS[i]
        #     else:
        #         return dfs(i-1, curr)
                
        # mx=0
        # for i in range(n-1,-1,-1): # run LIS from each index
        #     for j in range(i,-1,-1):
        #         if nums[j]<nums[i]:
        #             LIS[i] = 1 + dfs(j,nums[j])
        #     mx=max(mx,LIS[i])

        # return mx

        # THIS FAILED in 17th / 24 test case
        # BUT at least it was not greedy and there was some implimentation bug or an overlooked bug
        
        # n=len(nums)
        # LIS=[-1]*n
        # LIS[0]=1
        # def f(i):
        #     # print(f"=========================")
        #     # print(f"at idx = {i}, LIS[{i}] = {LIS[i]}")
        #     if LIS[i]!=-1: return LIS[i]
        #     LIS[i]=1
        #     for j in range(i-1,-1,-1):
        #         if nums[j]<nums[i]:
        #             # print(f"FOUND SMALLER than {i}, at j={j}")
        #             # print(f"Recursing at j={j} ")
        #             LIS[i]=max(LIS[i],f(j)+1)
        #             # print(f"f(j)={f(j)}")
        #             # print(f"LIS[{i}]={LIS[i]}")
        #         # else:
        #             # print(f"Skipping {j} ")
        #     # print(f"========== {i} over ===============")
        #     # print(f"LIS[{i}]={LIS[i]}")
        #     return LIS[i]
        # f(n-1)
        # mx=0
        # for i in range(n):
        #     mx=max(mx,LIS[i])
        # return mx

        n=len(nums)
        LIS=[1]*n
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    LIS[i]=max(LIS[i],LIS[j]+1)
        print(LIS)
        mx=0
        for i in range(n):
            mx=max(mx,LIS[i])
        return mx
