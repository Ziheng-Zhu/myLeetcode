lst = [{'age': 20}, {'age': 23}]
print(max(lst, key=lambda x: x['age']))
# {'age': 23}

salaries={
    'jasn':30090,
    'nancy':100000,
    'jack':10000,
    'nick':2090
}
# 匿名函数
print('工资最多的人是:', max(salaries, key=lambda x: salaries[x]))
#>>> nancy

t=[1,5,-6,-4]
ans=max(t,key=lambda k:abs(k))
print(ans) #-6

str1 = 'Life is short , I use python and mathematica'
print(str1.split())
print(max(str1.split(), key = len))

x='i want a banana'
ans=max(x.split(),key=lambda k:sum(ord(c) for c in k))
print(ans) #’banana’