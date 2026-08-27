class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        i,j=0,1
        while j<len(prices):
            if (prices[j]-prices[i])<=-1:
                i+=1
                j=i+1
            else:
                m=max(prices[j]-prices[i],m)
                j+=1
        return m