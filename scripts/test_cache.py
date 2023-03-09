from functools import lru_cache
from timeit import timeit

def slow_tuple_check(tup1, tup2):
    match_or_not = {"Match" : 0, "No Match" : 0}
    
    for item in tup1:
        for item2 in tup2:
            if item == item2:
                match_or_not["Match"] += 1
                
    print(match_or_not)
    
@lru_cache(maxsize=None)
def fast_tuple_check(tup1, tup2):
    match_or_not = {"Match" : 0, "No Match" : 0}
    
    for item in tup1:
        for item2 in tup2:
            if item == item2:
                match_or_not["Match"] += 1
                
    print(match_or_not)
    
huge_tup1 = tuple(range(1000))
huge_tup2 = tuple(range(1000))

print(timeit(lambda: slow_tuple_check(huge_tup1, huge_tup2), number=10))
print(timeit(lambda: fast_tuple_check(huge_tup1, huge_tup2), number=10))
print(timeit(lambda: slow_tuple_check(huge_tup1, ((1,2,3),(2,3,4),([1,2],[5,6]))), number=10))