# Here's an example of how you might write a Python function to calculate the number of possible 3D lattice paths from a starting point (0, 0, 0) 
# to an ending point(nx, ny, nz) without using any packages:


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def lattice_paths(nx, ny, nz):
    return comb(nx + ny + nz, nx) * comb(ny + nz, ny)
