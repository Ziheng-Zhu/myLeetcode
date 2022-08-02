def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

print(list(enumerate(['f','d','t'])))
print(list)