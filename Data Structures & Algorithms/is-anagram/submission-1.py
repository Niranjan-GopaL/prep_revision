from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        arr=[0]*26
        for i in s:
            arr[ord(i)-97]+=1

        for i in t:
            if arr[ord(i)-97]==0: return False
            arr[ord(i)-97]-=1
            
        for i in range(26):
            if arr[i]!=0: return False
        
        return True