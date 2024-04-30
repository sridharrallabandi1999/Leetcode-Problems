class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binearysearch(nums,target,True)
        right = self.binearysearch(nums,target,False)
        return(left,right)

    def binearysearch(self , nums,target,leftbias):
            start = 0
            i =-1
            end = len(nums)-1
            while start <= end:
                mid = (start + end )//2
                if target > nums[mid]:
                    start = mid +1
                elif target < nums[mid]:
                    end = mid -1
                else:
                    i = mid
                    if leftbias:
                        end = mid-1
                    else:
                        start = mid+1
            return i 


            