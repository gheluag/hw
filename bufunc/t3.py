from random import sample
def honnest(x):
    return x % 2 == 0
rnd = (sample(range(0, 21), 20))
rnd.sort(reverse = False)
rnd = map(int, rnd)
print(*filter(honnest,  rnd))