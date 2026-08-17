class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        res=[]
        for i in range(len(nums)):
            d[nums[i]]-=1
            if i and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                d[nums[j]]-=1
                if j-1>i and nums[j]==nums[j-1]:
                    continue
                tar=-(nums[i]+nums[j])
                if d[tar]>0:
                    res.append([nums[i], nums[j], tar])
            for j in range(i+1,len(nums)):
                d[nums[j]]+=1
        return res
            