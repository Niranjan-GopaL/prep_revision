class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # sm = 0 # this was my mistake
        sm = n
        for i in range(n):
            sm = sm ^ nums[i] ^ i
        return sm

