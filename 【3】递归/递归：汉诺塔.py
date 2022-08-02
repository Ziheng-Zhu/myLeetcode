# 有三根柱子：第一根柱子有若干块石块，从下往上重量依次递减
# 目标是从地一根柱子，把这些石块搬到第三根柱子上，每次移动要保持每根柱子上的石块从下往上依次递减

def moveTower(disk,p1,p2,p3):
    if disk >=1:
        moveTower(disk-1,p1,p3,p2)
        print(f'moving disk[{disk}] from {p1} to {p3}')
        moveTower(disk-1,p2,p1,p3)

moveTower(3,'#1','#2','#3')