"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
# Runtime: 28 ms
# Memory Usage: 12 MB


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mL = []
        mR = []
        n = len(height)
        if(n==0):
            return 0
        mL.append(height[0])
        for i in range(1,n):
            if(height[i] > mL[i-1]):
                mL.append(height[i])
            else:
                mL.append(mL[i-1])
                
        rev_height = height[::-1]
        mR.append(rev_height[0])
        for j in range(1,n):
            if(rev_height[j] > mR[j-1]):
                mR.append(rev_height[j])
            else:
                mR.append(mR[j-1])
    
        mR.reverse()
        w = []
        sum_w = 0
        for k in range(n):
            w.append(min(mL[k],mR[k])-height[k])
        for val in w:
            sum_w +=val
            
        return sum_w

 


