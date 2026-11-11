class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        ht={}
        window_size=0
        for r in range(len(s)):
            if s[r] in ht:
                l=max(ht[s[r]]+1,l)
            ht[s[r]]=r
            window_size=max(window_size,r-l+1)

        return window_size
            

        