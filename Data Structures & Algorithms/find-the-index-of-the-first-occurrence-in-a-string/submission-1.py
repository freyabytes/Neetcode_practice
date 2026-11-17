class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in haystack:
        #     if needle in haystack:
        #         return i
        # return -1
        n,m=len(haystack),len(needle)
        if n<m:
            return -1
        for i in range(n-m+1):
            j=0
            while j<m:
                if haystack[i+j]!=needle[j]:
                    break
                j+=1
            if j==m:
                return i
        return -1

        