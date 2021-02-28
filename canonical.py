import numpy as np
import to_latex

def canonical(A, b, c, z, B):
    A_B = A[:,B]
    A_B_inv = np.linalg.inv(A_B)
    A_B_inv_trans = np.transpose(A_B_inv)
    c_B = c[B]
    y = A_B_inv_trans.dot(c_B)
    
    new_A = A_B_inv.dot(A)
    new_b = A_B_inv.dot(b)
    new_c = np.transpose(np.transpose(c) - np.transpose(y).dot(A))
    new_z = (np.transpose(y).dot(b) + z)[0,0]
    
    
    #print('Written in canonical form with the basis $B = \{' +  B.__str__()[1:-1] + '\}$ is: \\\\ \n')
    #print('max $' + to_latex.bmatrix(np.transpose(new_c)) + 'x + ' + new_z.__str__() + '$ \\\\ \n')
    #print('s.t. \\\\ \n$' + to_latex.bmatrix(new_A) + 'x = ' + to_latex.bmatrix(new_b) + '$\\\\ \n' + '$x \\geq\\mathbb{O}$ \\\\ \n')

    return (new_A, new_b, new_c, new_z)

# sef = "Standard Equity Form"
#  at the moment, just multiplies c by -1 if is_min == True
#  TODO: figure out how to deal with inequalities and handling other weird things that may occur when trying to get into SEF
def sef(A, b, c, z, is_min):
    new_c = c
    if(is_min):
        new_c = -1 * new_c

    return(A, b, new_c, z)

""" tests
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
z = 3
basis_arr = [1, 3]
print(canonical(A, b, c, z, basis_arr))
"""