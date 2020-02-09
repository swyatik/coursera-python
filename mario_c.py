import sys

num_steps = int(sys.argv[1])
hash_s = 1
for i in range(num_steps):
    for hashes in range(num_steps - hash_s):
        print(" ", end='')
    for spaces in range(hash_s):
        print("#", end='')
    print()
    hash_s += 1

