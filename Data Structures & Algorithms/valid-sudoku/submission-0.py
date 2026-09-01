class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row wise check
        for i in board:
            seen={}
            for j in i:
                if j!='.' and j in seen:
                    return False
                seen[j]=1+seen.get(j,1)
        for i in range(len(board)):
            seen={}
            for j in range(len(board[i])):
                v=board[j][i]
                if v!='.' and v in seen:
                    return False
                seen[v]=1+seen.get(v,1)
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
