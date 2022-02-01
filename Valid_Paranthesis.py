"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

"""

"""https://leetcode.com/problems/valid-parentheses/"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i  not in dic:
                stack.append(i)
            else:
                if(len(stack)>0):
                    p=stack.pop()
                    print(p)
                    if(dic[i]!=p):
                        return False
                else:
                    return False
        if(len(stack)>0):
            return False
        return True
                