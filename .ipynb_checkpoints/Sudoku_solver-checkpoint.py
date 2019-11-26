import copy

class Solution:

    def main(self): 
        q = input(">>")
        q = eval(q)
        self.sudoku(q)
        return

    def sudoku(self, q):
        all_ans = {}
        for i in range(9):
            for j in range(9):
                if q[i][j]==0:
                    all_ans[(i,j)]={1,2,3,4,5,6,7,8,9}
                    for k in range(9):
                        if q[i][k]!=0:
                            (all_ans[(i,j)]).discard(q[i][k])
                    for k in range(9):
                        if q[k][j]!=0:
                            (all_ans[(i,j)]).discard(q[k][j])
                    for k in range(3):
                        for l in range(3):
                            if q[(i//3)*3+k][(j//3)*3+l]!=0:
                                (all_ans[(i,j)]).discard(q[(i//3)*3+k][(j//3)*3+l])
                else:
                    all_ans[(i,j)] = {q[i][j]}    

        ans = self.fill_sudoku(all_ans, 0, 0)
        print (ans)

    def fill_sudoku(self, now_ans, i, j):
        
        if len(now_ans[(i,j)])==0:
            return 0
        if i==8 and j==8:
            if len(now_ans[(i,j)])==1:
                return now_ans
            else:
                return 0
        i_next = i
        j_next = j
        if j<8:
            j_next += 1
        elif i<8:
            j_next = 0
            i_next += 1

        for ans in now_ans[(i,j)]:
            now_ans_next = copy.deepcopy(now_ans)
            now_ans_next[(i,j)]={ans}
            for k in range(9):
                if k!=j:
                    (now_ans_next[(i,k)]).discard(ans)
            for k in range(9):
                if k!=i:
                    (now_ans_next[(k,j)]).discard(ans)
            for k in range(3):
                for l in range(3):
                    if (i//3)*3+k!=i and (j//3)*3+l!=j:
                        (now_ans_next[((i//3)*3+k,(j//3)*3+l)]).discard(ans)

            answer = self.fill_sudoku(now_ans_next, i_next, j_next)

            if (answer!=0):
                return answer
                
        return 0


sudoku_solution = Solution()
sudoku_solution.main()