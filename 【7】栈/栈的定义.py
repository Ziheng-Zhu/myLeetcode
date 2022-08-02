#from pythonds.basic.stack import  Stack

# s = Stack()
#
# print(s.isEmpty())
# print(s.items)
# s.push(5)
# print(s.peek())

# 自己写一段ADT Stack代码
class Stack():

    # 定义Stack的属性：
    def __init__(self):
        self.items = []

    # 判断Stack是否为空
    def isEmpty(self):
        return self.items == []

    # 给Stack添加元素
    def push(self, item):
        self.items.append(item)

    # 删除Stack最先添加的元素
    def pop(self):
        return self.items.pop()

    # 查看（返回）Stack最先添加的元素
    def peek(self):
        return self.items[len(self.items)-1]

    # 返回Stack对象的size
    def size(self):
        return len(self.items)