import canonical
import simplex
import numpy as np
import to_latex

def q2():
    A = np.array([
        [-2, -1, 3, 9],
        [-1, -1, 2, 2],
        [2, 2, -1, -5],
        [1, 1, -1, -2],
        [-1, 0, 1, 2],
        [3, 2, -3, -8],
        [0, 1, 1, 5],
        [1, 1, -1, -2]
    ])

    b = np.array([
        [9],
        [-2],
        [6],
        [3],
        [4],
        [1],
        [15],
        [3]
    ])


    A_ = np.array([
        [-1, -1, 2, 2],
        [2, 2, -1, -5],
        [1, 1, -1, -2],
        [-1, 0, 1, 2],
        [1, 1, -1, -2]
    ])

    # print(np.linalg.matrix_rank(A_))

    b_ = np.array([
        [-2],
        [6],
        [3],
        [4],
        [3]
    ])

    x = np.array([
        [-1],
        [7],
        [1],
        [1]
    ])

    # res = np.dot(A, x)

def q2b():

    A_ = np.array([
        [-1, -1, 2, 2],
        [2, 2, -1, -5],
        [1, 1, -1, -2],
        [-1, 0, 1, 2],
        [1, 1, -1, -2]
    ])

    # print(np.linalg.matrix_rank(A_))

    b_ = np.array([
        [-2],
        [6],
        [3],
        [4],
        [3]
    ])

    x = np.array([
        [5],
        [2],
        [-2],
        [3]
    ])

    A = np.array([
        [-2, -1, 3, 9],
        [-1, -1, 2, 2],
        [2, 2, -1, -5],
        [1, 1, -1, -2],
        [-1, 0, 1, 2],
        [3, 2, -3, -8],
        [0, 1, 1, 5],
        [1, 1, -1, -2]
    ])

    b = np.array([
        [9],
        [-2],
        [6],
        [3],
        [4],
        [1],
        [15],
        [3]
    ])

    d = np.array([
        [1],
        [-2],
        [-3],
        [1]
    ])

    x3 = x + 0.5 * d
    x4 = x - 0.5 * d

    print(to_latex.pmatrix(0.5 * x3))
    print(to_latex.pmatrix(0.5 * x4))
    print(to_latex.pmatrix(0.5 * (x4 + x3)))

def test():
    print(to_latex.pmatrix(A_))
    print(to_latex.pmatrix(x))
    print('\\leq')
    print(to_latex.pmatrix(b_))

    c = np.array([
        [1],[2],[3],[4]
    ])
    z = 0
    # B = [0, 1, 2]

    B = simplex.find_feasible_basis(A, b)

    # to_latex.print_lp(A, b, c, z)
    A, b, c, z = canonical.canonical(A, b, c, z, B)
    to_latex.print_lp(A, b, c, z)

def q3():
    A = np.array([
        [1, 1, 0, -1, 2],
        [3, 0, 1, -2, 5]
    ])

    b = np.array([
        [5],
        [15]
    ])

    c = np.array([
        [3],[0],[0],[-2],[1]
    ])

    z = 0

    B = [1,2]

    B = simplex.find_better_basis(A, b, c, z, B)
    A, b, c, z = canonical.canonical(A, b, c, z, B)
    B = simplex.find_better_basis(A, b, c, z, B)
    A, b, c, z = canonical.canonical(A, b, c, z, B)
    
    to_latex.print_lp(A, b, c, z)

q3()