class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # naive approach O( N * sum(wegiths)) try out all limits between max(weights) and sum(weights)
        # better : O(Nlog(sum(weights)))
        
        mx=-1
        sm=0
        for i in weights:
            mx=max(i,mx)
            sm+=i

        # can we ship all packages with this limit in <= "days" days
        def condition(limit):
            required_days=0
            sm=0
            for i in weights:
                sm+=i
                if sm  > limit:
                    required_days+=1
                    sm=i
                    if required_days > days :
                        return False
            required_days+=1
            if required_days > days :
                return False
            return True

        # Answer space : [mx, ..... sm]
        # Answer space : [0 0 0 0 1 1 1 1 1 1] left will have the first occurance of 1
        left=mx
        right=sm

        while left<right:
            mid=left+(right-left)//2

            if condition(mid):
                right=mid
            else:
                left=mid+1
        
        return left