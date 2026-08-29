class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        ct={}
        for c in t:
            ct[c]=1+ct.get(c,0)
        win={}
        have=0
        need=len(ct)
        res,rl=[-1,-1], float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            win[c]=1+win.get(c,0)
            if c in ct and win[c]==ct[c]:
                have+=1
            while have==need:
                if (r-l+1)<rl:
                    res=[l,r]
                    rl=r-l+1
                win[s[l]]-=1
                if s[l] in ct and win[s[l]]<ct[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if rl!=float("inf") else ""
            
        