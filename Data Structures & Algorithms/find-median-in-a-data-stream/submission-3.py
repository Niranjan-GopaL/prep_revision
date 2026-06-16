import heapq

# PERFECT EXAMPLE OF LOGIC WHERE IT'S INSANE that 
# ======> the ORDER IN WHICH WE CHECK leads to DRAMATICALLY different code.
# it is soo fricking hard to get this correct.



class MedianFinder:

    def __init__(self):
        # KEY idea : 
        #    - 1st half of sorted array should be in MX_HP ( max heap )
        #    - 2nd half of sorted array should be in MN_HP ( min heap )
        #  
        #  we will maintain min_heap and max_heap
        # [ every time we insert, we make sure both heap sizes are same. ]

        #   Insertion :
        #  if elem < first_half : 
        #       first_half.insert(elem)
        #  elif elem > second_half
        #       second_half.insert(elem)

        self.first_half = []  # MAX_heap
        self.second_half = [] # MIN_heap
        self.median=0
        self.n=0

    def addNum(self, num: int) -> None:

        if self.n == 0 :
            heapq.heappush(self.first_half, -num)
            self.n+=1
            self.median=num
            return
       
        if self.n & 1 : 
            # if arr length "WAS" odd, we can make both half have same count
            
            if len(self.first_half) == len(self.second_half) + 1:
                if num < -self.first_half[0] :
                    head=-heapq.heappop(self.first_half)
                    heapq.heappush(self.first_half, -num)
                    heapq.heappush(self.second_half,head)
                else:
                    heapq.heappush(self.second_half,num)

            elif len(self.second_half) == len(self.first_half) + 1 :
                if num<-self.first_half[0] or (num<self.second_half[0]):
                    heapq.heappush(self.first_half, -num)
                
                else:
                    head=heapq.heappop(self.second_half)
                    heapq.heappush(self.second_half ,num)
                    heapq.heappush(self.first_half,-head)

            self.median = ( -self.first_half[0] + self.second_half[0] ) / 2

        else:
            # if arr len "WAS" even, then we have a choise to make
            if num < -self.first_half[0] :
                heapq.heappush(self.first_half, -num)
                self.median = -self.first_half[0] 
            else:
                heapq.heappush(self.second_half, num)
                self.median = self.second_half[0]
        self.n+=1


    def findMedian(self) -> float:
        return self.median
        
        