class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # what is the string built in functions to upper case / lower case / other immportant fns

        # l=0
        # n=len(s)
        # r=n-1

        # def is_alpha_numeric(c):
        #     return (97<=ord(c)<=97+26-1) or (65<=ord(c)<=65+26-1) or (48<=ord(c)<=48+10-1) 

        # # a string that has no alphanumeric will also be palindorme since alphanumeric part is ""
        # while 0<= l < r < n:
            
        #     while (0<=l<n) and not is_alpha_numeric(s[l]):
        #         l+=1
        #     while (0<=r<n) and not is_alpha_numeric(s[r]):
        #         r-=1
            
        #     if (0<= l < r < n) and s[l].upper() != s[r].upper():
        #         return False
        #     l+=1
        #     r-=1

        # return True

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True