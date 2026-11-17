class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Left sum = sum of everything before i
        #Right sum = sum of evrything after i
        left=0
        total=sum(nums)
        for i in range(len(nums)):     
            right=total-left-nums[i]
            if left ==right:
                return i
            left+=nums[i]
        return -1
