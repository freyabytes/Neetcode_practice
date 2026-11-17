class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  zxyzxyz
        #  |-|->zxy no dupes len 3
        #   |-|->xyz no dupes len 3
        #    |-|->yzx no dupes len 3
        #    ...
        # we can solve it with hashset and then sliding window
        
        # Approach: sliding window over s, tracking the current window (no dupes)
        # - left pointer `l` marks the start of the window
        # - initialise to set to keep count of the unique characters
        # - move `r` across s one char at a time:
        #     * if s[r] is NOT in the set -> just add it
        #     * if s[r] IS in the set    -> shrink from the LEFT:
        #         remove s[l], l+=1, repeat until s[r] is gone from the set
        # - after each step, window size = r - l + 1, update the max length
        # - return the max length

        max_length=0
        store=set()
        left=0

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[left])
                left+=1
            store.add(s[r])
            max_length=max(max_length,r-left+1)
        return max_length





