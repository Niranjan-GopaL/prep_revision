class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # didn't read the question properly
        # freq=[0]*26
        # for i in t:
        #     freq[ord(i)-97]+=1
        # for i in s:
        #     if freq[ord(s)-97] == 0 : return False 
        #     freq[ord(s)-97]-=1
        # return True
        m=len(s)
        n=len(t)
        if m>n: return False
        if m==0 and n==0: return True

        j=0
        i=0
        while i<m :
            while j<n:
                if t[j]==s[i]: 
                    break
                j+=1
            if j==n and i<m: return False
            i+=1
            j+=1
        return True