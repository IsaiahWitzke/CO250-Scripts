import canonical
import numpy as np
import to_latex

def find_dual(A, b, c, z):
    dual_A = np.transpose(A)
    dual_b = c
    dual_c = -1 * b
    if (z != 0):
        raise NotImplementedError()
    dual_z = z
    return (dual_A, dual_b, dual_c, dual_z)

def test():
    A = np.array([
        [5, 4, 3, 2, 1],
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8, 10],
        [1, 0, 1, 0, 1]
    ])

    b = np.array([
        [3],
        [1],
        [4],
        [1]
    ])

    c = np.array([
        [1],
        [2],
        [3],
        [4],
        [5]
    ])

    z = 0

    (A_, b_, c_, z_) = find_dual(A, b, c, z)

    to_latex.print_lp(A, b, c, z)
    to_latex.print_lp(A_, b_, c_, z_)

def q2():
    A_P = np.array([
        [2, 0, -1],
        [2, -1, -1],
    ])

    b_P = np.array([
        [3],
        [5]
    ])

    c = np.array([
        [4],
        [0],
        [-1]
    ])

    y = np.transpose(np.array([
        [1],
        [-1]
    ]))

    A_D = np.transpose(A_P)

    u_transpose = np.array([1,0,2])

    print(to_latex.pmatrix(np.dot(u_transpose, A_D)))
    print(to_latex.pmatrix(np.dot(u_transpose, c)))

q2()
# test()
