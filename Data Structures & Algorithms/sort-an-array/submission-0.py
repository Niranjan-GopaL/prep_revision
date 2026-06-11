class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # 1. convert nums into a heap O(n)
        # 2. I will swap root with last element
        # 3. Then last element is in it's correct position. 
        # 4. Now I will call heapify upto len-2 index (len-1 is  in correct)
        
        # so parent > children
        def max_heapify(heap,i,heap_size):
            l,r,largest = 2*i+1,2*i+2,i
            if l<heap_size and heap[l] > heap[largest]: largest=l
            if r<heap_size and heap[r] > heap[largest]: largest=r
            if largest!=i:
                heap[largest],heap[i]=heap[i],heap[largest]
                max_heapify(heap,largest,heap_size)

        # O(n) conversion to heap
        for idx in range(len(nums)//2-1,-1,-1):
            max_heapify(nums,idx,len(nums))

        # print(nums)

        for idx in range(len(nums)-1,-1,-1):
            nums[idx],nums[0]=nums[0],nums[idx]
            # print(nums, idx)
            max_heapify(nums,0,idx)

        return nums

