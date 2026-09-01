class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row wise check
        for i in range(len(board)):
            cseen={}
            rseen={}
            for j in range(len(board[i])):
                vc=board[j][i]
                vr=board[i][j]
                if vc!='.' and vc in cseen:
                    return False
                cseen[vc]=1+cseen.get(vc,1)
                if vr!='.' and vr in rseen:
                    return False
                rseen[vr]=1+rseen.get(vr,1)
        #For the box 
        i=0
        j=0
        while i<=8:
            while j<=8:
                if j%3==0:
                    seen={}
                if board[i][j]!='.' and board[i][j] in seen:
                    return False
                seen[board[i][j]]=1
                if board[i+1][j]!='.' and board[i+1][j] in seen:
                    return False
                seen[board[i+1][j]]=1
                if board[i+2][j]!='.' and board[i+2][j] in seen:
                    return False
                seen[board[i+2][j]]=1
                j+=1
            i+=3
            j=0
        return True