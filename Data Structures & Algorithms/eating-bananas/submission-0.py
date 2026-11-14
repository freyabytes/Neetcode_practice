class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        result=right
        while left<=right:
            k=(left+right)//2
            total_hours=0
            for p in piles:
                total_hours +=(p+k-1)//k
            if total_hours<=h:
                result=k
                right=k-1
            else:
                left=k+1
        return result
           