class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # failed attempts
        # a = int('0b' + a)
        # a = int('0b' + b)
        
        # DO NOT FORGET THIS
        a = int(a,2)
        b = int(b,2)

        while b!=0 : 
            sm    = a ^ b
            carry = a & b
            a = sm
            b = carry << 1 
        return bin(a)[2:]