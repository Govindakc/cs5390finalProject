from time import time
def edit_distance_recursive(i, j):
    if len(i) == 0: return len(j)
    if len(j) == 0: return len(i)
    if i[-1] != j[-1]:
        D = 1
    else:
        D = 0
    d = edit_distance_recursive(i[:-1], j[:-1]) + D 
    v = edit_distance_recursive(i[:-1], j) + 1
    h = edit_distance_recursive(i, j[:-1]) + 1
    return min(d, v, h)


st = time()
print(edit_distance_recursive("TTACTGTGTTT", "CACCCCTGTG"))
print('Took %0.3f seconds' % (time() - st))
