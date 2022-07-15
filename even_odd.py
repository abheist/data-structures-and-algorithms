from typing import List


def even_odd(a: List[int]) -> List[int]:
    next_even, next_odd = 0, len(a) - 1
    while next_even < next_odd:
        print('running')
        if a[next_even] % 2 == 0:
            next_even += 1
        else:
            a[next_even], a[next_odd] = a[next_odd], a[next_even]
            next_odd -= 1
    return a


print(even_odd([1, 2, 2, 1]))

