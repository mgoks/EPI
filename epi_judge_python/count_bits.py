from test_framework import generic_test

# O(N) time and space in the number of bits of x
def count_bits(x: int) -> int:
    n = 0
    while x > 0:
        n += x & 1
        x >>= 1
    return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
