"""
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

#Runtime: 32 ms
#Memory Usage: 10.8 MB



class Solution(object):
    
    def reverse(self, nums, start):
        i = start, j = n
        while(i<j):
            swap(nums, i,j)
            i +=1
            j -=1
    
    def swap(self, nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        a = 0
        target = 0
        i = n-1
        while(i >=0  and nums[i+1] <= nums[i]):
            i -= 1
        
        if(i >= 0):
            j = n
            while(j>=0 and nums[j] <= nums[i]):
                j -= 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        p = i+1
        j = n
        while(p<j):
            temp = nums[p]
            nums[p] = nums[j]
            nums[j] = temp
            p +=1
            j -=1
