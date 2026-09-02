class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up,down=0,len(matrix)-1

        def search_row(row, target):
            left,right=0,len(row)-1
            while left<=right:
                mid=(left+right)//2
                if row[mid]==target:
                    return True
                elif row[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return False

        while up<=down:
            row=(up+down)//2
            if matrix[row][0]<=target<=matrix[row][-1]:
                return search_row(matrix[row],target)
            elif target<matrix[row][0]:
                down=row-1
            else:
                up=row+1
        return False