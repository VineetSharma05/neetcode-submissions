class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        res=[1]
        pos=1
        for i in nums:
            pre=pre*i
            res.append(pre)
        res=res[:-1]
        for j in range(len(nums)-1,-1,-1):
            res[j]=res[j]*pos
            pos=pos*nums[j]
        return res