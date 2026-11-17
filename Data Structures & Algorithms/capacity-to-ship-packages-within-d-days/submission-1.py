class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def canship(cap):
            curr_cap=cap
            ship=1
            for w in weights:
                if curr_cap - w<0:
                    ship+=1
                    curr_cap=cap
                curr_cap-=w
            return ship<=days

        while l<=r:
            cap=(l+r)//2
            if canship(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res
