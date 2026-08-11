class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=set()
        for i in range(len(nums)):
            if nums[i] not in d:
                d.add(nums[i])
            else:
                return True 
        return False
