class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            current_weight = 0
            count = 1
            for w in weights:
                if current_weight + w > mid:
                    count += 1
                    current_weight = 0
                current_weight += w
            if count <= days:
                right = mid
            else:
                left = mid + 1
                
        return left