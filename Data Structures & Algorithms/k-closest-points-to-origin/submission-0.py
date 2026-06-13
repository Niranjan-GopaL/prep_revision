class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            if not points: return []
            if len(points)<=k: return points

            # 1. create a min heap  O( n logn )
            # 2. heap pop k times  

            def insert(heap,x,y):
                d=x*x+y*y
                heap.append((d,[x,y]))
                i = len(heap)-1
                # if child < parent => swap (it's a min heap)
                while i>0 and  heap[i][0]<heap[(i-1)//2][0] :
                    heap[(i-1)//2],heap[i]=heap[i],heap[(i-1)//2]
                    i=(i-1)//2

            def pop(heap):
                ans=heap[0][1]
                heap[0]=heap[-1]
                heap.pop()
                i=0
                n=len(heap)
                while 1:
                    l,r,smallest=2*i+1,2*i+2,i
                    if l<n and heap[l][0]<heap[smallest][0]: smallest=l
                    if r<n and heap[r][0]<heap[smallest][0]: smallest=r
                    if smallest!=i:
                        heap[smallest],heap[i]=heap[i],heap[smallest]
                        i=smallest
                    else:
                        break
                return ans

            # step 1
            heap=[]
            for point in points:
                insert(heap,point[0],point[1])

            print(heap)

            # step 2
            ans=[]
            for _ in range(k):
                ans.append(pop(heap))

            print(ans)
            return ans