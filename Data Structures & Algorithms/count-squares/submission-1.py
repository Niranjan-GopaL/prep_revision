from collections import defaultdict

class CountSquares:

    def __init__(self):
    # 1. mapsx is hashmap with key : value=hashmap ( Hashmap of Hashmaps )
    # 2. when I get a point (x,y) : I will add x in mapsx and y in mapsy
    # 3. in O(1) I can query if a certain y or x ever existed (without error) 
    #    in our data structure as well as update the count of that point's occurance 
    # 4. If I want to query(qx,qy) = find total number of ways to create square 
    # Sum of all cnt1*cnt2*cnt3 is the final answer.
        self.mapsx=defaultdict(dict)
        self.mapsy=defaultdict(dict)

    def add(self, point: List[int]) -> None:
        x,y=point

        if x in self.mapsx :
            if y in self.mapsx[x]:
                self.mapsx[x][y]+=1
            else:
                self.mapsx[x][y]=1
        else:
            self.mapsx[x][y]=1
        
        if y in self.mapsy :
            if x in self.mapsy[y]:
                self.mapsy[y][x]+=1
            else:
                self.mapsy[y][x]=1
        else:
            self.mapsy[y][x]=1
        
    print("1")
    def count(self, point: List[int]) -> int:
        qx,qy=point
        if (qy not in self.mapsy) or (qx not in self.mapsx) : return 0
        # so there are both qx and qy available in the ds.
        ans=0
        for x,cnt1 in self.mapsy[qy].items():
            side = x-qx
            if side and (qy+side in self.mapsx[qx]) and (qy+side in self.mapsx[x]): 
                cnt2 = self.mapsx[qx][qy+ side]
                cnt3 = self.mapsx[x][qy + side]
                ans+=cnt1*cnt2*cnt3    
                print(ans)
            if side and (qy-side in self.mapsx[qx]) and (qy-side in self.mapsx[x]): 
                cnt2 = self.mapsx[qx][qy - side]
                cnt3 = self.mapsx[x][qy - side]
                ans+=cnt1*cnt2*cnt3
        return ans
                
                


        
