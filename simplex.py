import canonical
import numpy as np
import to_latex

def find_better_basis(A, b, c, z, B):
    all_elems = np.array(range(0, A.shape[1]))
    N = np.setxor1d(all_elems, B)
    c_N = c[N,:]
    
    # if cN <= 0, then stop, the basic solution x is optimal 
    c_N_leq_0 = True
    for c_N_elem in c_N:
        if(c_N_elem[0] > 0):
            c_N_leq_0 = False
    if(c_N_leq_0):
        print('STOP! $c_N = ' + to_latex.bmatrix(c_N) + ' \\leq 0$. The basic solution $\\bar{x}$ is optimal')
        return
    
    # pick k not in B such that c_k > 0 and set x_k = t
    k = -1
    for i in N:
        k = i
        if(c_N[k,0] > 0):
            break
    
    print('We choose $k = ' + (k + 1).__str__() + '$ to be the new element that will be added to the basis. This is because $c_' + (k + 1).__str__() + ' = ' + c[k,:].__str__()[1:-1] + ' > 0$, and k is the smallest element that satisfies this constraint (Bland\'s rule)\\\\ \n')

    A_k = A[:,[k]]

    # if A_k is leq 0, then STOP, the LP is unbounded
    A_k_leq_0 = True
    for A_k_elem in A_k:
        if(A_k_elem[0] > 0):
            A_k_leq_0 = False
    if(A_k_leq_0):
        print('STOP! $A_k = ' + to_latex.bmatrix(A_k) + ' \\leq 0$. The LP is unbounded')
        return
    
    # choose t to be the min of some stuff...
    possible_t_vals = []
    
    for i in range(0, b.size):
        if(A_k[i] <= 0):
            continue
        else:
            possible_t_vals.append(b[i,0] / A_k[i])

    t = min(possible_t_vals)

    print('$t = min\{' + possible_t_vals.__str__()[1:-1] + '\} = ' + t.__str__() + '$ \\\\ \n')

    new_x_B = b - (t * A_k)

    print('$x_B = b - tA_k = ' + to_latex.bmatrix(b) + ' - ' + t.__str__() + to_latex.bmatrix(A_k) + ' = ' + to_latex.bmatrix(new_x_B) + '$ \\\\ \n')

    r = -1
    for i in range(0, A_k.shape[0]):
        if(new_x_B[i] == 0):
            r = B[i]
            break
    
    print('This means that $r = ' + (r + 1).__str__() + '$. This is the smallest 0-element index of the new $x_B$ - we are using Bland\'s rule\\\\ \n')
    
    better_B = np.sort(
        np.append(
            np.setxor1d(B, np.array(r)),    # remove r from the basis
            k                               # add k to the basis
        )
    )
    
    print('This means that our better basis is $B = \{' + better_B.__str__()[1:-1] + '\}$. \\\\ \n')
    return better_B


def simplex_pt_1(A, b, c, z, B):
    return 0

A = np.array([
        [1, 1, 2, 0],
        [0, 1, 1, 1]
])
b = np.array([
        [2],
        [5]
])
c = np.array([
    [0],
    [1],
    [3],
    [0]
])
z = 0
basis_arr = [0, 3]

new_basis = find_better_basis(A, b, c, z, basis_arr)
new_A, new_b, new_c, new_z = canonical.canonical(A, b, c, z, new_basis)

print('new A: \n' + new_A.__str__() + '\n')
print('new b: \n' + new_b.__str__() + '\n')
print('new c: \n' + new_c.__str__() + '\n')
print('new z: \n' + new_z.__str__() + '\n')
