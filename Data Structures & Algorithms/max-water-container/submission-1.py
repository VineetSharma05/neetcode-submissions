class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a=0
        l=0
        r=len(heights)-1
        while l<=r:
            a=max(a,min(heights[l],heights[r])*(r-l))
            if heights[l]<=heights[r]:
                l=l+1
            else:
                r-=1
        return a

        