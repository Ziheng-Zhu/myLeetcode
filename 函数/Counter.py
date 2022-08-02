from collections import Counter

x = [1,2,3,4,5,5,3,3,4]
count = Counter(x)
for i,j in count.items():
    print(i,j)
print(count)
print(type(count))