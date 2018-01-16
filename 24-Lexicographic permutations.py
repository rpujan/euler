from itertools import permutations
perms = [''.join(p) for p in permutations('0123456789')]
print(perms[999999]) # one millionth combination

# 2783915460