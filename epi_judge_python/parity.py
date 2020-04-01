from test_framework import generic_test


# brute force O(N) time in the number of bits of x
# def parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= x & 1     # equivalent to  result = (result + x&1) % 2
#         x >>= 1
#     return result

# O(K) time in the number of set bits in x, K < N
def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
