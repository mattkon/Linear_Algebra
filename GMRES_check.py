# Matthew Konyndyk
# Math 343 Winter 2017
# Final Project Part 2






### DESCRIPTION OF ASSIGNMENT ######################################################################

# Part 2: Use some of the functions from your library, for an appropriately given input matrix A, and
# 1. Implement the GMRES algorithm with restart (provided in a separate .pdf file).
# 2. Perform study when you vary mmax = 5, 10, 15, ... the maximal number of steps allowed in the algorithm, and document the total number of iterations and total time to convergence for a given tolerance  (and a given matrix). Write your conclusions from the study.

### BACKGROUND INFORMATION ON LEAST SQUARES ########################################################

# Least Squares: if A*x=b has no solution, you can find the least squares approximation using the formula (A^T)*A*(x`)=(A^T)*b
# This will minimize the distance ||b-A*x`|| betwen the least squares solution and the solution we wanted.
# Note - A*(x`) is the projection of b onto the column space of A.

# Gram Schmidt: Given a Matrix with arbitray basis, Gram Schmidt creates an orthonormal basis.

# QR decomposition: Q - Orthogonal Matrix, R - Upper Triangular Matrix; R = (Q^T)*M
# Using QR to solve least squares: R*x = (Q^T)*b


### GMRES ALGORITHM: An Iterative Least Squares Algorithm ##########################################

# Krylov Subspace - the order-r Krylov subspace generated by an n-by-n matrix A and a vector b of dimension n is the linear subspace spanned by the images of b under the first r powers of A (starting from  A^{0}=I), that is the span {b,(A)b,(A^2)b,...,(A^(r-1))b} https://en.wikipedia.org/wiki/Krylov_subspace

# Arnoldi Iteration - an eigenvalue algorithm and an important example of iterative methods. Arnoldi finds the eigenvalues of general (possibly non-Hermitian) matrices. Arnoldi belongs to a class of linear algebra algorithms (based on the idea of Krylov subspaces) that give a partial result after a relatively small number of iterations. Arnoldi iteration is a typical large sparse matrix algorithm: It does not access the elements of the matrix directly, but rather makes the matrix map vectors and makes its conclusions from their images. This is the motivation for building the Krylov subspace. https://en.wikipedia.org/wiki/Arnoldi_iteration

# GMRES - generalized minimal residual method (GMRES) is an iterative method for the numerical solution of a nonsymmetric system of linear equations. The method approximates the solution by the vector in a Krylov subspace with minimal residual. The Arnoldi iteration is used to find this vector. https://en.wikipedia.org/wiki/Generalized_minimal_residual_method

# We start with an initial approximation guess x0 (x0 is arbitray, I begin with zeros.) we also have input tolerance (e) and number of iterations(m_max)

# The algorithm will stop once ||b-A*x`|| < e, or m_max has been reached


import scipy as sp
import numpy as np
import time




def GMRES(A, b, x0, e, m_max, restart): #Finds numerical solution to a nonsymmetric system of linear equations. Useful for sparse matrices, because of the relatively low  systemmemory it requires.
    
    #initialize values
    x = [] # initializes return vector
    q = [0] * (m_max) # initializes Krylov subspace
    h = np.zeros((m_max + 1, m_max)) #used in Arnoldi iteration?
    restartsleft = restart
    residual = 1
    iterations = 0

    #begin
    while restartsleft > 0 and residual > e:
        r = b - np.asarray(sp.dot(A, x0)).reshape(-1) # initial residual, reshaped to a vector
        x.append(r)
        q[0] = r / np.linalg.norm(r) #initial residual normalized
        
        #The Arnoldi iteration uses the stabilized Gram Schmidt process to find orthonormal vectors, q1, q2, q3, ..., called the Arnoldi vectors, such that for every n, q1, ..., qn span the Krylov subspace. https://en.wikipedia.org/wiki/Arnoldi_iteration
        
        for k in range(m_max): #changes from wikipedia algorithm: q[k] = q[k-1], y = q[k]
            if residual > e:
            
                y = np.asarray(sp.dot(A, q[k])).reshape(-1) #A.normalized residual
                for j in range(k):
                    h[j, k] = np.dot(q[j], y) #fills out the m+1 x m matrix with q(j).q(k)
                    y = y - h[j, k] * q[j]
                h[k + 1, k] = np.linalg.norm(y)
                if (h[k + 1, k] != 0 and k != m_max - 1): q[k + 1] = y / h[k + 1, k] #q(k) = q(k)/h(k,k-1)
            
                c = np.zeros(m_max + 1)
                c[0] = np.linalg.norm(r) #c is [norm(r), 0, 0, ... 0]
                result = np.linalg.lstsq(h, c)[0]
                x.append(np.dot(np.asarray(q).transpose(), result) + x0)
                residual = np.linalg.norm(b - np.asarray(sp.dot(A, (np.dot(np.asarray(q).transpose(), result) + x0))).reshape(-1))
                iterations += 1
        if residual > e:
            restartsleft -= 1
            x0 = x[-1:] #resets x0 before next restart
    
    return x, restart-restartsleft, residual, iterations



#GMRES ALGORITHM

#Matrix A , solution b, initial guess x0
size = 10
A = np.random.random((size, size)) #creates random 5x5 matrix
b = np.random.random(size) #creates random solution vector
x0 = np.zeros(size) #initial approximation. This might also be a random vector.
#tolerances
e = 1e-3
m_max = 100
restart = 20
#begin
start = time.time() #start timer
result, rest, residual, iterations = GMRES(A, b, x0, e, m_max, restart)
end = time.time() #end timer
#print(result)
print '\n', 'random', size, 'x', size, 'Matrix A: '
print A
print 'random solution vector b: '
print b
print '\n', 'GMRES: ', m_max, 'iterations per cycle,', rest, 'restarts, and', iterations, 'total iterations'
print 'Time to coverge: ', end - start
print 'residual: ', residual
print result[-1:]



#CHECK USING SCI PY

from scipy.sparse.linalg import gmres
result2 = gmres(A,b,x0)
print '\n', 'Check using Scipy: '
print result2[0]
