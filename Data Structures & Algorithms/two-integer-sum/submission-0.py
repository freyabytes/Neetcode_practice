class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,n in enumerate(nums):
            num_needed=target-n
            if num_needed in seen:
                return [seen[num_needed],i]
            seen[n]=i