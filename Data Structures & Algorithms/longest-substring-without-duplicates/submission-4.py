class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        t=''
        m=0
        while i<len(s):
            if s[i] not in t:
                t+=s[i]
                i+=1
            else:
                t=t[1:]
            m=max(m,len(t))
        return m

        