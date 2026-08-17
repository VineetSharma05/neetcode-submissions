class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i and a==numbers[i-1]:
                continue
            l=i
            r=len(numbers)-1
            while l<r:
                if numbers[l]+numbers[r]>target:
                    r-=1
                elif numbers[l]+numbers[r]<target:
                    l+=1
                else:
                    return [l+1, r+1]
        