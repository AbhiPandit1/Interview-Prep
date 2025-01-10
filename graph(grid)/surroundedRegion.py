# reverse thinking wala question he basically question kehta he chaaro direction me X ho O ke to wo X ban jyega
# but boundary kabhi aise ni hoga ku uska ek direction always empty hota he
# so islie hum saare boundary wale O leke aur usse jo jo connected use mark krlenge thk iske lie bfs linkenge
# mark ke lie alg naamd dedo Y
# phr jaayenge border pe bfs traverse krenge
# atlast jo jo Y he use O bama denge and jo O hoga use X

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m=len(board)
        n=len(board[0])

        def helper(i,j):

            if i<0 or j<0 or i>=m or j>=n or board[i][j]!="O":
                return 
            
            board[i][j]="Y"

            directions=[[0,1],[0,-1],[1,0],[-1,0]]

            for dr,dc in directions:
                helper(i+dr,j+dc)
        

        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=="O":
                    helper(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="Y":
                    board[i][j]="O"
        return board
