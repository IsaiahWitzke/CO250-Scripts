import numpy as np

def pmatrix(a):
    """Returns a LaTeX pmatrix

    :a: numpy array
    :returns: LaTeX pmatrix as a string

    See: https://stackoverflow.com/questions/17129290/numpy-2d-and-1d-array-to-latex-pmatrix
    """
    if len(a.shape) > 2:
        raise ValueError('pmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{pmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{pmatrix}']
    return '\n'.join(rv)

def print_lp(A, b, c, z):
    print('max $' + pmatrix(np.transpose(c)) + 'x + ' + z.__str__() + '$ \\\\ \n')
    print('s.t. \\\\ \n\n$' + pmatrix(A) + 'x = ' + pmatrix(b) + '$\\\\ \n\n' + '$x \\geq\\mathbb{O}$ \\\\ \n\n')