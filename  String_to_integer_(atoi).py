"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        ss=("0","1","2","3","4","5","6","7","8","9"," ","+","-")
        if( len(s)==0 or s[0] not in ss ):
            return 0
        found=0
        sign=None
        res=""
        for i in range(len(s)):
            if(s[i] not in ss):
                return 0
    
            elif(s[i] in ("-","+") or (ord(s[i]) >=48 and ord(s[i])<=58)):
                if(s[i]=="-"):
                    sign="-"
                if(s[i] in ("-","+")):
                    i+=1
                j=i
                while(j<len(s) and ord(s[j])>=48 and ord(s[j])<=58):
                    res+=s[j]
                    j+=1
                break
        if(len(res)==0):
            return 0
        res=int(res)
        if(sign !=None):
            res*=-1
        return  min(max(int(res), -2147483648), 2147483647)   
   
                