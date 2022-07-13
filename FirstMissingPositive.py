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
    
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        N = len(nums) 
        for i in range(N):
            if nums[i] <= 0 or nums[i] > N:
                nums[i] = N + 1
        
        
      
        for i in range(N):
            v = abs(nums[i]) 
            print(v)
            if v-1 < N and nums[v-1] > 0:
                nums[v-1] = -nums[v - 1]
        
        # After the transformations, any positive number in array indicates a missing number in range 1 to N
        # Take the first found positive value, if any
        # Time: O(N)
        for i in range(N):
            print(nums[i])
            if nums[i] > 0:
                return i+1

      
        return N+1
"""
