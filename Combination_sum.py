"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
"""https://leetcode.com/problems/combination-sum/"""
# from collection import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        resu=[]
        def rec(n,sum,l):
            if(sum==target):
                resu.append(l.copy())
                return
            if(n<0):
                return
            if(sum>target):
                return
            print(n)
            l.append(candidates[n])
            rec(n,sum+candidates[n],l)
            l.pop()
            rec(n-1,sum,l)
        rec(len(candidates)-1,0,[])
        return resu