class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
                # print(f"original : {arr}")
        
        def lower_bound_bin_search(arr, target):
            low, high = 0, len(arr)     # Note: high is exclusive
            while low < high:
                mid = low + (high - low) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low  # First position where arr[i] >= target

        lower_bound = lower_bound_bin_search(arr,x)
        left=lower_bound-k if lower_bound-k >= 0 else 0 
        right=lower_bound+k if lower_bound+k <= len(arr)-1 else len(arr)-1
        # print(f"{lower_bound} | {left} | {right}\n")

        heap=[]

        # reutrns 1 if parent is closer than child
        def check(x, parent, child):
            if abs(parent-x) < abs(child-x): return 1
            elif abs(parent-x) == abs(child-x) and parent<child : return 1
            else : return 0

        def close_heap_push(heap,elem,x):
            heap.append(elem)
            idx=len(heap)-1
            while idx > 0:
                p_idx = (idx - 1) // 2
                if not check(x, parent=heap[p_idx], child=heap[idx]):
                    heap[p_idx], heap[idx] = heap[idx], heap[p_idx]
                    idx = p_idx
                else:
                    break

        # pop and heapify
        def close_heap_pop(heap,x):
            ans=heap[0]
            if len(heap) > 1:
                heap[0]=heap.pop()
                i=0
                while 1:
                    l=2*i+1
                    r=2*i+2
                    smallest=i
                    if l<len(heap) and not check(x, parent=heap[smallest], child=heap[l]) : smallest = l
                    if r<len(heap) and not check(x, parent=heap[smallest], child=heap[r]) : smallest = r
                    if smallest != i:
                        heap[smallest],heap[i] = heap[i], heap[smallest]
                        i=smallest
                    else:
                        break
            else:
                heap.pop()
            return ans

        for i in range(left,right+1):
            close_heap_push(heap,arr[i],x)

        ans=[]
        for _ in range(k):
            ans.append(close_heap_pop(heap,x))
        return sorted(ans)