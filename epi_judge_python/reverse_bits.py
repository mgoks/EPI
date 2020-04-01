from test_framework import generic_test

PRECOMPUTED_REVERSE = {}

def swap_bits(x, i, j):
    if (x>>i) & 1 != (x>>j) & 1:
        x ^= (1 << i) | (1 << j)
    return x

max_size = 16   # max size for precomputed values
for num in range(1 << max_size):
    i, j, rev = 0, max_size-1, num
    while i < j:
        rev = swap_bits(rev, i, j)
        i, j = i+1, j-1
    PRECOMPUTED_REVERSE[num] = rev

# O(N/L) time where N = the size of x, L = max size of cache key
# For this implementation N = 64, L = 16; therefore O(1)
def reverse_bits(x: int) -> int:
    """
    x is 64 bit integer. Divide it into 4 parts of 16 bits: x3, x2, x1, x0. 
    Let y = reverse_bits(x) = f(x). Then y would be f(x0), f(x1), f(x2), and
    f(x3) ORed together.
    """
    mask = 0xFFFF
    y3 = PRECOMPUTED_REVERSE[x & mask]
    y2 = PRECOMPUTED_REVERSE[(x >> 16) & mask]
    y1 = PRECOMPUTED_REVERSE[(x >> 32) & mask]
    y0 = PRECOMPUTED_REVERSE[x >> 48]
    return (y3<<48) | (y2<<32) | (y1<<16) | y0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
