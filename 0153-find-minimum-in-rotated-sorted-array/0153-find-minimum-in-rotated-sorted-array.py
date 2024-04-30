class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        minimum = sys.maxsize

        while left <= right:
            mid = (left+right)//2
            if nums[left]<=nums[mid]:
                minimum = min(minimum,nums[left])
                left = mid+1
            else:
                minimum = min(minimum,nums[mid])
                right = mid - 1
        return minimum
        """
        :type nums: List[int]
        :rtype: int
        """
        