class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        pivot=l
        temp=tuple(nums)
        temp1=list(temp[pivot:])+list(nums[0:pivot])
        def bs(left,right,num):
            while left<=right:
                mid=(left+right)//2
                if num[mid]==target:
                    return mid
                elif num[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        res=bs(0,len(nums)-1,temp1)
        if res!=-1:
            return (bs(0,len(nums)-1,temp1)+pivot)%len(nums)
        return -1