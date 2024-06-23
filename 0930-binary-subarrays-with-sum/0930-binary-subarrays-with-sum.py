class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        res = 0
        mp = defaultdict(int)
        prefix = 0
        mp[0] = 1  
        for num in nums:
            prefix += num
            res += mp[prefix - goal]  
            mp[prefix] += 1  
        return res
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """