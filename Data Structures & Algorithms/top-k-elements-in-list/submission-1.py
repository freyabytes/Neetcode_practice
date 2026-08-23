class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n]=1
        sorted_items=sorted(seen.items())

        res=[]
        for _ in range(k):
            max_freq=-1
            max_num=None
            for num,freq in seen.items():
                if freq>max_freq:
                    max_freq=freq
                    max_num=num
            res.append(max_num)
            del seen[max_num]
        return res

            