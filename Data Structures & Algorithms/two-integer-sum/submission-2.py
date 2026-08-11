class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,1
        while i<len(nums)-1 and j<len(nums):
            if nums[i] + nums[j]==target:
                return [i,j]
            elif j<len(nums)-1:
                j+=1
            else:
                i=i+1
                j=i+1