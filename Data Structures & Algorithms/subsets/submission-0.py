class Solution:
    def subsets(self, nums):
        res = []
        current = []
        def backtrack(i):
            if i == len(nums):
                res.append(current.copy())
                return
            # TAKE nums[i]
            current.append(nums[i])
            backtrack(i + 1)
            # UNDO
            current.pop()
            # DON'T TAKE nums[i]
            backtrack(i + 1)
        backtrack(0)
        return res