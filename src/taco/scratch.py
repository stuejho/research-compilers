# Import the TACO Python library
import pytaco as pt
from pytaco import dense, compressed

# Declare a new tensor of double-precision floats with dimensions 
# 512 x 64 x 2048, stored as a dense-sparse-sparse tensor
A = pt.tensor([512, 64, 2048], pt.format([dense, compressed, compressed]), pt.float64)

# Write tensor A to file "A.tns"
pt.write("A.tns", A)

dm   = pt.format([dense, dense])                        # (Row-major) dense matrix format
csr  = pt.format([dense, compressed])                   # Compressed sparse row matrix format
csc  = pt.format([dense, compressed], [1, 0])           # Compressed sparse column matrix format
dcsc = pt.format([compressed, compressed], [1, 0])      # Doubly compressed sparse column matrix format
csf  = pt.format([compressed, compressed, compressed])  # Compressed sparse fiber tensor format

# Declare a sparse tensor
A = pt.tensor([512, 64, 2048], compressed)

# Set A(0, 1, 0) = 42.0 + 24.0 = 66.0
A.insert([0, 1, 0], 42.0)
A.insert([0, 1, 0], 24.0)

for coordinates, val in A:
    print(val)