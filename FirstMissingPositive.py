"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""
# Runtime: 24 ms
# Memory Usage: 10.8 MB

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = []
        for num in nums:
            if(num > 0):
                pos.append(num)
        f = 0
        pos.sort()
        dict_m = {}
        for num in pos:
            if(num not in dict_m):
                dict_m[num] = num
        
        new_p = []
        for key in dict_m:
            new_p.append(key)
    
        new_p.sort()
        print(new_p)
        for i in range(len(new_p)):
            if(new_p[i]!=i+1):
                return i+1
            f = new_p[i]
        return f+1
