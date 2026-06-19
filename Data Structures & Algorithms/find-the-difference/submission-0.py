# Convert a lowercase letter
# print(ord('a'))   # Output: 97
# The inverse: converting an ASCII code back to text
# print(chr(65))    # Output: 'A' # note that it's CHR AND NOT CHAR


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if not s : return t
        if not t : return s
        # so now both s and t has some characters 
        xor = 0
        for char in s:
            xor ^= (ord(char)) 
        for char in t:
            xor ^= (ord(char)) 
        return chr(xor)