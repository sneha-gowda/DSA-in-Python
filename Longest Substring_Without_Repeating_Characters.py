"""Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3."""
"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        dic={}
        cnt=0
        maxi=0
        while(j<len(s)):
            if(s[j] in dic and dic[s[j]]==0):
                cnt+=1
                dic[s[j]]+=1
                j+=1
            elif(s[j] not in dic):
                cnt+=1
                dic[s[j]]=1
                j+=1
            else:
                while s[i]!=s[j]:
                    dic[s[i]]-=1
                    cnt-=1
                    i+=1
                i+=1
                j+=1
            maxi=max(maxi,cnt)
        return maxi
                