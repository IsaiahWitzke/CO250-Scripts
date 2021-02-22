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
    
    print('The LP: \\\\ \n max $' + to_latex.bmatrix(np.transpose(c)) + 'x + ' + z.__str__() + '$ \\\\ \n')
    print('s.t. \\\\ \n$' + to_latex.bmatrix(A) + 'x = ' + to_latex.bmatrix(b) + '$\\\\ \n' + '$x \\geq\\mathbb{O}$ \\\\ \n')
    print('Written in canonical form with the basis $B = \{' +  B.__str__()[1:-1] + '\}$ is: \\\\ \n')
    print('max $' + to_latex.bmatrix(np.transpose(new_c)) + 'x + ' + new_z.__str__() + '$ \\\\ \n')
    print('s.t. \\\\ \n$' + to_latex.bmatrix(new_A) + 'x = ' + to_latex.bmatrix(new_b) + '$\\\\ \n' + '$x \\geq\\mathbb{O}$ \\\\ \n')

    return (new_A, new_b, new_c, new_z)
    

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