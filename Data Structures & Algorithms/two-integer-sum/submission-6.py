class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        #adding the diff of target and the current val as key and the index as value
        for i in range(len(nums)):
            dif=target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[dif]=i
        