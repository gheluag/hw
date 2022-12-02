def alphabet():
    por = (d for d in range(1,27))
    bukv = (b for b in range(97,123))
    for i,j in zip(por,bukv):
        print(i, chr(j))

alphabet()

print()
#словарь

def alph():
    dct = {key : chr(value) for key,value in zip(range(1,27), range(97, 123))}
    print(dct)
alph()