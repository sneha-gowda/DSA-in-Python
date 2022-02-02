"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

"""
"""https://leetcode.com/problems/search-in-rotated-sorted-array/"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                return mid
            elif(nums[0]<=nums[mid]):
                if(target<nums[mid] and target>=nums[0]):
                    high=mid-1
                else:
                    low=mid+1
            elif(nums[mid]<=nums[len(nums)-1]):
                if(target>nums[mid] and target<=nums[len(nums)-1]):
                    low=mid+1
                else:
                    high=mid-1
        return -1