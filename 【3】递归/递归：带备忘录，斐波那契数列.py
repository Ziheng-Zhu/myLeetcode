
# 用递归来实现斐波那契数列
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#print(fib(5))
# 算法复杂度太高了，而且有重复计算，所以可以考虑把重复计算的保存起来

def fib1(n):
    if n<1:
        return 0
    memo = [0]*(n+1)
    return helper(memo,n)

def helper(memo,n):
    if n==1 or n==2:
        memo[n] =1
    if memo[n]!=0:
        return memo[n]
    memo[n] = helper(memo,n-1) + helper(memo,n-2)
    print(memo)
    return memo[n]

#print(fib1(10))

# 上面这种带备忘录的是自顶向下，就是说原问题逐渐分解为更小规模的问题

# 也可以考虑自底向上，从边界条件出发考虑原问题

def fib2(n):
    f = [0]*(n+1)
    for i in range(1,n+1):
        if i==1 or i==2:
            f[i] = 1
        else:
            f[i] = f[i-1] + f[i-2]
    return f
print(fib2(10))

# 进一步优化，实际上并不需要这么长的数列来存储，因为斐波那契数列只需要保存前两布

def fib3(n):
    if n==1 or n==2:
        return 1
    pre = 1
    cur = 1
    for i in range(3,n+1):
        temp = cur
        cur = pre+cur
        pre = temp
    return cur

print(fib3(10))


