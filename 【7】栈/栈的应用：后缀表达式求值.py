from pythonds.basic.stack import Stack

def postEval(postExpr):
    numStack = Stack()
    tokenList = postExpr.split()

    for token in tokenList:
        if token in '0123456789':
            numStack.push(int(token))
        else:
            num1 = numStack.pop()
            num2 = numStack.pop()
            num = op(token,num1,num2)
            numStack.push(num)
    return numStack.pop()

def op(token,num1,num2):
    if token == '+':
        return num1 + num2
    elif token == '-':
        return num1 - num2
    elif token == '*':
        return num1 * num2
    elif token =='/':
        return num1/num2

print(postEval(' 5 4 + 3 *'))