#Generators in pyhton
#A generator is a function that produces values one at a time instead of computing and storing all values at once in memory.

import sys

# ---- Basic Generator ----

def count_up(start, end):
    """Generates numbers from start to end one at a time"""
    current = start
    while current <= end:
        yield current       # pause, send current value, resume later
        current += 1

gen = count_up(1, 5)

print("--- Using next() manually ---")
print(next(gen))            # 1
print(next(gen))            # 2
print(next(gen))            # 3

print("\n--- Using for loop (recommended way) ---")
for num in count_up(1, 5):  # for loop calls next() automatically
    print(num)


# ---- Practical Example: Reading a huge file line by line ----

def read_large_file(filepath):
    """
    Generator to read a file one line at a time.
    Useful when file is too large to load entirely into memory.
    """
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()    # yield one line at a time

# Usage — only one line lives in memory at a time
# for line in read_large_file("bigfile.txt"):
#     print(line)


# ---- Infinite Generator ----

def infinite_counter(start=0):
    """Generates numbers forever — only possible with generators"""
    num = start
    while True:             # infinite loop — fine because yield pauses it
        yield num
        num += 1

counter = infinite_counter()
print("\n--- Infinite counter (first 5 values) ---")
for _ in range(5):
    print(next(counter))    # 0, 1, 2, 3, 4


# ---- Memory Comparison ----

def list_of_numbers(n):
    """Normal function — stores all n numbers in memory"""
    return [i for i in range(n)]

def gen_of_numbers(n):
    """Generator — stores only ONE number at a time"""
    for i in range(n):
        yield i

n = 1000000

list_size = sys.getsizeof(list_of_numbers(n))
gen_size  = sys.getsizeof(gen_of_numbers(n))

print(f"\n--- Memory Usage for {n} numbers ---")
print(f"List size:      {list_size:,} bytes")   # ~8 million bytes
print(f"Generator size: {gen_size:,} bytes")    # ~200 bytes  ✅
