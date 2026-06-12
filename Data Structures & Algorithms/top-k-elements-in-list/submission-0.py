from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        min_heap = []
        for key, v in freq_map.items():
            heapq.heappush(min_heap, (v, key))

        ans = []
        for _, key in heapq.nlargest(k, min_heap):
            ans.append(key)

        return ans