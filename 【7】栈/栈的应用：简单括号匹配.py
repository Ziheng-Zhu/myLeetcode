from pythonds.basic.stack import Stack

def parChecker1(symStr):

    s = Stack()
    balanced = True
    index = 0

    while index<len(symStr) and balanced:
        symbol = symStr[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker1(')()('))
print(parChecker1('(())'))


def parChecker2(symStr):

    s = Stack()
    balanced = True
    index = 0

    while index<len(symStr) and balanced:
        symbol = symStr[index]
        if symbol in '{([':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top =  s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(parChecker2('[{()}]'))
print(parChecker2('[{(})]'))