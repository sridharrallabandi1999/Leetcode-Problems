class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        if n==1:
            return 0
         
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1

        left = 1
        right = n-2
        while left <=right:
            mid = (left+right)//2
            if(mid ==0 or nums[mid-1]<nums[mid]) and (mid ==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            if nums[mid]>=nums[mid-1]:
                left = mid+1
            else:
                right = mid-1

                
        return -1 
        """
        :type nums: List[int]
        :rtype: int
        """
        