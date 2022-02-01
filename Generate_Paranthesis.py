"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
"""https://leetcode.com/problems/generate-parentheses/"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def rec(o,c,s):
            if(c==n):
                res.append(s)
                return
            if(o>c):
                rec(o,c+1,s+")")
            if(o<n):
                rec(o+1,c,s+"(")
        rec(0,0,"")
        return res
        