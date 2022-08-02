from pythonds.basic.stack import Stack


def trans(num,base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while num !=0:
        rem = num%base
        s.push(rem)
        num = num//base
    binStr = ''
    while not s.isEmpty():
        binStr = binStr + str(digits[s.pop()])
    return binStr

print(trans(47,16))
