class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in haystack:
        #     if needle in haystack:
        #         return i
        # return -1
        if needle=="":
            return 0

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
               
        return -1
        