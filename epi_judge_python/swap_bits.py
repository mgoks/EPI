from test_framework import generic_test


# def swap_bits(x: int, i: int, j: int) -> int:
#     """
#     Only swap if ith bit is 0 and jth bit is 1 or vice versa.
#     If the bit is set, AND it with ~(1<<i); else, OR it with 1<<i.
#     """
#     bit_i, bit_j  = (x>>i) & 1, (x>>j) & 1
#     if bit_i and not bit_j:
#         x = x & ~(1<<i)
#         x = x |  (1<<j)
#     elif bit_j and not bit_i:
#         x = x & ~(1<<j)
#         x = x |  (1<<i)
#     return x
    
# using XOR
def swap_bits(x: int, i: int, j: int) -> int:
    if (x>>i) & 1 != (x>>j) & 1: 
        x ^= (1<<i) | (1<<j)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
