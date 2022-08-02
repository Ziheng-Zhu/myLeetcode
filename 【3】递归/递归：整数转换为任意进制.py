
def toStr(n,base):
    converStr = '0123456789ABCDEF'
    if n < base:
        return converStr[n]
    else:
        return toStr(n//base,base) + converStr[n%base]