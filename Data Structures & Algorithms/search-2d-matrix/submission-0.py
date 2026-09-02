class Solution(object):
    def searchMatrix(self, matrix, target):
        col=len(matrix[0])
        row=len(matrix)
        l=0
        right=row*col-1
        while l<=right:
            mid=(right+l)//2
            r=mid//col
            c=mid%col
            v=matrix[r][c]
            if v==target:
                return True
            elif v<target:
                l=mid+1
            else:
                right=mid-1
        return False

        