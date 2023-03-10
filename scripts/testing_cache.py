def rem():
    for _ in range(10000):
        big_list = [((0, 0), (0, 1), (1, 1), (1, 0)),
                    ((0, 0), (5, 1), (1, 1), (1, 0)),
                    ((0, 0), (0, 1), (1, 1), (1, 6))]
        big_list.remove(((0, 0), (5, 1), (1, 1), (1, 0)))

def pop2():
    for _ in range(10000):
        big_list = [((0, 0), (0, 1), (1, 1), (1, 0)),
                    ((0, 0), (5, 1), (1, 1), (1, 0)),
                    ((0, 0), (0, 1), (1, 1), (1, 6))]
        big_list.pop(1)
        
import timeit

print(timeit.timeit(rem, number=10000))
print(timeit.timeit(pop2, number=10000))