class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        if len(s)!=len(t):
            return False

        for char_s in s:
            if char_s not in seen:
                seen[char_s]=1
            else:
                seen[char_s]+=1
            
        for char_t in t:
            if char_t not in seen or seen[char_t]==0:
                return False
            seen[char_t]-=1
        return True

        