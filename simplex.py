import canonical
import numpy as np
import to_latex

class OptimalBasicSolution(Exception):
    def __init__(self, B):
        self.B = B
        super().__init__()

class UnboundedSolution(Exception):
    pass

class NoSolution(Exception):
    pass

# AKA, the major part of "PHASE 2" of simplex (requires that A, b, c, z, B are in canoncal form)
def find_better_basis(A, b, c, z, B):
    """
    AKA, the major part of "PHASE 2" of simplex (requires that A, b, c, z, B are in canoncal form)
    """
    all_elems = np.array(range(0, A.shape[1]))
    N = np.setxor1d(all_elems, B)
    c_N = c[N,:]

    # if cN <= 0, then stop, the basic solution x is optimal 
    c_N_leq_0 = True
    for c_N_elem in c_N:
        if(c_N_elem[0] > 0):
            c_N_leq_0 = False
    if(c_N_leq_0):
        print('STOP! $c_N = ' + to_latex.pmatrix(c_N) + ' \\leq 0$. The basic solution $\\bar{x}$ is optimal')
        raise OptimalBasicSolution(B)
    
    # pick k not in B such that c_k > 0 and set x_k = t
    k = -1
    for i in range(0, c.size):
        if(i in B):
            continue
        a = c[i,0]
        if(a > 0):
            k = i
            break
    
    # print('We choose $k = ' + (k + 1).__str__() + '$ to be the new element that will be added to the basis. This is because $c_' + (k + 1).__str__() + ' = ' + c[k,:].__str__()[1:-1] + ' > 0$, and k is the smallest element that satisfies this constraint (Bland\'s rule)\\\\ \n')

    A_k = A[:,[k]]

    # if A_k is leq 0, then STOP, the LP is unbounded
    A_k_leq_0 = True
    for A_k_elem in A_k:
        if(A_k_elem[0] > 0):
            A_k_leq_0 = False
    if(A_k_leq_0):
        print('STOP! $A_k = ' + to_latex.pmatrix(A_k) + ' \\leq 0$. The LP is unbounded')
        # TODO: print out the "certificate"
        raise UnboundedSolution()
    
    # choose t to be the min of some stuff...
    possible_t_vals = []
    
    for i in range(0, b.size):
        if(A_k[i] <= 0):
            continue
        else:
            possible_t_vals.append(b[i,0] / A_k[i])

    t = min(possible_t_vals)

    # regex seems to hate me... fix me later
    # print('$t = min\{' + possible_t_vals.__str__()[1:-1].replace(r"[array\(\)\[\]]", '') + '\} = ' + t.__str__()[1:-1] + '$ \\\\ \n')

    new_x_B = b - (t * A_k)

    # print('$x_B = b - tA_k = ' + to_latex.pmatrix(b) + ' - ' + t.__str__() + to_latex.pmatrix(A_k) + ' = ' + to_latex.pmatrix(new_x_B) + '$ \\\\ \n')

    r = -1
    for i in range(0, A_k.shape[0]):
        if(new_x_B[i] == 0):
            r = B[i]
            break
    
    # print('This means that $r = ' + (r + 1).__str__() + '$. This is the smallest 0-element index of the new $x_B$ (by choosing this element, we are adhering to Bland\'s rule)\\\\ \n')
    
    better_B = np.sort(
        np.append(
            np.setxor1d(B, np.array(r)),    # remove r from the basis
            k                               # add k to the basis
        )
    )
    
    # print('This means that our "better basis" is $B = \{' + better_B.__str__()[1:-1] + '\}$. \\\\ \n')
    return better_B


def find_optimal_solution(A, b, c, z, B):
    try:
        while(True):
            B = find_better_basis(A, b, c, z, B)
            A, b, c, z = canonical.canonical(A, b, c, z, B)
            to_latex.print_lp(A, b, c, z)
    except OptimalBasicSolution as soln:
        return (A, b, c, z, B)

def find_feasible_basis(A, b):
    aux_variables = np.eye(A.shape[0])
    A_with_aux = np.append(A, aux_variables, axis=1)
    B = np.array(range(A.shape[1], A_with_aux.shape[1]))
    # neg to turn the "min x_4 + x_5" into a "max -x_4 - x_5"
    aux_c = -1 * np.array([np.append(
        np.zeros((1, A.shape[1])),
        np.ones((1, A.shape[0]))
    )]).T
    z = 0
    bfs = np.append(np.zeros((1, A.shape[1])), np.transpose(b))
    print('We now have the auxiliary LP\\\\ \\n')
    to_latex.print_lp(A_with_aux, b, aux_c, z)
    print('With BFS as: $\\bar{x} = ' + to_latex.pmatrix(bfs) + '$.\\\\ \n')


    canon_A, canon_b, canon_c, canon_z = canonical.canonical(A_with_aux, b, aux_c, z, B)
    new_A, new_b, new_c, new_z, new_B = find_optimal_solution(canon_A, canon_b, canon_c, canon_z, B)
    
    # if the aux elements in the "optimal" basis, then we know that there isn't any solution
    for orig_basis_elem in B:
        if(orig_basis_elem in new_B):
            y = np.dot(np.linalg.inv(np.transpose(A_with_aux[:,B])), c[B])
            print('This LP is not feasible. Here is the certificate: $y = ' + to_latex.pmatrix(y) + '$.')
            raise NoSolution()
    return B


