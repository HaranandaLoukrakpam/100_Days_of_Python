import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

# Example 1: Check version

print("-----------------------------------------------------------")
print("NumPy version:", np.__version__)
print("-----------------------------------------------------------")

# Example 2: Create a tiny array and inspect it

print("Array:", a, "| dtype:", a.dtype, "| ndim:", a.ndim, "| shape:", a.shape)         #.dtype prints the data-type, .ndim prints the dimension, .shape prints the shape i,e row x column
print("-----------------------------------------------------------")

# Example 3: Simple math without loops (vectorized)

print("Vectorized add:", a + b)   # elementwise
print("Vectorized *2:", a * 2)
print("-----------------------------------------------------------")

# Example 4: Reproducible random numbers using seed

np.random.seed(42)
print("Random numbers:", np.random.randint(0, 10, size=5))                              #randint prints random integer, rand p
print("-----------------------------------------------------------")
# ---- From Python sequences ----

# Example 1: From list (1D)
a1 = np.array([1, 2, 3, 4])
print("From list:", a1, "| dtype:", a1.dtype)
print("-----------------------------------------------------------")

# Example 2: From nested list (2D matrix)
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", a2)
print("-----------------------------------------------------------")

# Example 3: From tuple with dtype
a3 = np.array((1.1, 2.2, 3.3), dtype=np.float32)
print("From tuple with dtype:", a3, "| dtype:", a3.dtype)
print("-----------------------------------------------------------")

# ---- Range-like builders ----

# Example 4: arange(start, stop, step)
r1 = np.arange(0, 10, 2)  # 0..8 step 2
print("arange:", r1)
print("-----------------------------------------------------------")

# Example 5: linspace(start, stop, num) inclusive endpoints
r2 = np.linspace(1,10,10)
print("linspace:", r2)
print(len(r2))
print("-----------------------------------------------------------")

# Example 6: logspace(start_exp, stop_exp, num) -> 10**exponent
r3 = np.logspace(0, 3, 3,base=10)  # 10^0 .. 10^3 with 4 points
print("logspace:", r3)
print("-----------------------------------------------------------")

# ---- special arrays ----
z = np.zeros((3,4))
o = np.ones((2, 3))
f = np.full((2, 3), fill_value="bhi")
print("zeros:\n", z)
print("-----------------------------------------------------------")
print("ones:\n", o)
print("-----------------------------------------------------------")
print("full(7):\n", f)
print("-----------------------------------------------------------")

# Example 8: Identity/eye + diagonal
I = np.eye(5)         # Identity
D = np.diag([5, 3, 2,12,54])  # Diagonal from 1D list
print("Identity:\n", I)
print("-----------------------------------------------------------")
print("Diagonal:\n", D)
print("-----------------------------------------------------------")

# Example 9: Random-based creation
np.random.seed(41)
rand_uniform = np.random.rand(2, 3)         # [0,1)
rand_normal  = np.random.randn(2, 3)        # standard normal
rand_ints    = np.random.randint(40, 50, size=(9,10))
print("rand uniform:\n", rand_uniform)
print("-----------------------------------------------------------")
print("rand normal:\n", rand_normal)
print("-----------------------------------------------------------")
print("rand ints:\n", rand_ints)
print("-----------------------------------------------------------")

#Reshape in numpy
arr1 = np.arange((18))
arr2 = arr1.reshape((1,9,2))
print(arr2)
print("-----------------------------------------------------------")

#slicing and indexing in python 
x = np.array([10, 20, 30, 40, 50, 60])
print("Tw dimensional array: ",x)
print("-----------------------------------------------------------")

# Example 1: Basic indexing
print("x[0] =", x[0], "| x[-1] =", x[-1])
print("-----------------------------------------------------------")

# Example 2: Slicing ranges
print("x[1:4] =", x[1:4])
print("x[:3]  =", x[:3])
print("x[3:]  =", x[3:])
print("-----------------------------------------------------------")

# Example 3: Step & reverse
print("x[::2]  =", x[::2])    # every 2nd
print("x[::-1] =", x[::-1])   # reverse
print("-----------------------------------------------------------")

# ---- 2D ----
A = np.arange(1, 13).reshape(3, 4)
print("Three dimensional array: ",A)
print("-----------------------------------------------------------")

# Example 4: Index specific item
print("A[0, 2] =", A[1,2])      # row 0, col 2 -> 3
print("-----------------------------------------------------------")

# Example 5: Entire row/col
print("Row 1:", A[1, :])         # 2nd row
print("Col 2:", A[:, 2])         # 3rd column
print("-----------------------------------------------------------")

# Example 6: Submatrix slice
print("Block A[0:2, 1:3]:\n", A[0:2, 1:3])  # rows 0-1, cols 1-2
print("-----------------------------------------------------------")

# ---- 3D ----
B = np.arange(2*3*4).reshape(2, 3, 4)  # (depth=2, rows=3, cols=4)
print(B)
print("-----------------------------------------------------------")

# Example 7: Indexing across 3 axes
print("B[1, 2, 3] =", B[1, 2, 3])
print("-----------------------------------------------------------")

# Example 8: Slice along last axis
print("B[:, 1, :]:\n", B[:, 1, :])
print("-----------------------------------------------------------")

# Example 9: Slice a 3D block
print("B[0:2, 0:2, 2:4]:\n", B[0:2, 0:2, 2:4])
print("-----------------------------------------------------------")




