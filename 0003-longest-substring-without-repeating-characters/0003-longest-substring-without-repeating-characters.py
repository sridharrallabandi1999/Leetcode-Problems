class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 1
        maxNum = 0
        for _ in s:
            while len(s[l:r]) != len(set(s[l:r])):
                l += 1
            
            print(s[l:r])
            maxNum = max(len(s[l:r]), maxNum)
            r+=1
        
        return maxNum
