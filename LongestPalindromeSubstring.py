# Given a string s, return the longest palindromic substring in s.
# Runtime: 64 ms
# Memory Usage: 10.9 MB


class Solution(object):
    def longestPalindrome(self,s):
        if len(s)==0:
            return s
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]   
