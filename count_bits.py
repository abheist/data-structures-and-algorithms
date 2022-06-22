def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

    printcount_bits(2))
    print(count_bits(4))
    print(count_bits(6))
