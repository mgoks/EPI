from test_framework import generic_test


# brute force O(N) time in the number of bits of x
# def parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= x & 1     # equivalent to  result = (result + x&1) % 2
#         x >>= 1
#     return result

# O(K) time in the number of set bits in x, K < N
def parity_slow(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result

precomputed_parity = [parity_slow(i) for i in range(0xFFFF)]

# O(1) time (excluding the time takes fill the look-up table)
def parity(x: int) -> int:
    mask = 0xFFFF   # 2^16 - 1
    x0 = precomputed_parity[x & mask]
    x1 = precomputed_parity[(x>>16) & mask]
    x2 = precomputed_parity[(x>>32) & mask]
    x3 = precomputed_parity[x>>48]
    return x3 ^ x2 ^ x1 ^ x0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
