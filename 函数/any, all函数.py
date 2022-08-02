#
#any(iterable)
# Return True if any element of the iterable is true.
# If the iterable is empty, return False. Equivalent to:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False



# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，
# 如果是返回 True，否则返回 False。
#
# 元素除了是 0、空、None、False 外都算 True。
#
# 函数等价于：

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True