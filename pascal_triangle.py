from char_transform import *



def generate_pascal_triangle(n: int):
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries.
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result







print()




def build_rings(n):
    def convert_to_num(L): return [ 1 if L[x]==1 else 0 for x in range(len(L)) ]
    def convert_to_sym(L): return [ '*' if L[x]==0 else ' ' for x in range(len(L)) ]

    a = [ (x+2) for x in range(8,408,2) ]
    b = [ x for x in range(1,201) ]
    index = { b[x]: a[x] for x in range(len(a)) }

    t1 = generate_pascal_triangle(index[n])

    for x in t1:
        print(x)
    print()

    for x in range(len(t1)):
        print(' ' * (len(t1)-x),t1[x])
    print()

    for x in range(len(t1)):
        print(' ' * (len(t1)-x),convert_to_num(t1[x]))
    print()

    t2 = []
    for x in range(9):
        del(t1[0])
    for x in range(len(t1)):
        for y in range(len(t1)-x):
            t1[x].reverse()
            t1[x].append(1)
        del(t1[x][-1])
        if (len(t1)-x)%2!=0:
            t2.append(convert_to_sym(convert_to_num(t1[x])))
            print(convert_to_num(t1[x]))

    print()

    for x in range(len(t2)):
        print(t2[x])

    print()

    for x in range(len(t2)):
        print(myConcat(t2[x]))

    print(' Total Rings:',len(t2))
    return
