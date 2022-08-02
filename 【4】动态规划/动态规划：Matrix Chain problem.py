
# Matrix Chain problem is to determine the parenthesization of the expression
# defining the product A that minimizes the total number of scalar multiplications performed.

def matrix_chain(d):

    n = len(d)-1
    N = [[0]*n for i in range(n)]
    for b in range(1,n):
        for i in range(n-b):
            j = i +b
            N[i][j] = min(N[i][k]+N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i,j))

    return N


## input: min(j for j in range(10))
## output : 0

## input: [0] *3
## ouput: [0,0,0]

print(matrix_chain([2,3,4]))