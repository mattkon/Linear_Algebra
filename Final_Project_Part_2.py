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
# Gram Schmidt: Given a Matrix with arbitray basis, Gram Schmidt creates an orthogonal basis.
# QR decomposition: Q - Orthogonal Matrix, R - Upper Triangular Matrix; R = (Q^T)*M
# Using QR to solve least squares: R*x = (Q^T)*b


### GMRES ALGORITHM: An Iterative Least Squares Algorithm ##########################################

# We start with an initial approximation guess x0 (x0 is arbitray, I begin with zeros.) we also have input tolerance (e) and number of iterations(m_max)
# The algorithm will stop once ||b-A*x`|| < e, or m_max has been reached


import scipy as sp
import numpy as np


def GMRES(A, b):
    e = .0001
    m_max = 50
    x = [] # initialize x
    p = [0] * (m_max) #creates list p
    R = np.zeros((m_max + 1, m_max)) #initialize a 50x51 matrix of zeros
 
 
 
    x0 = np.zeros(5) #initial approximation
    r = np.asarray(b - A.dot(x0)).reshape(-1) # r0 = b - A*x0 (intial residual - the distance between guesses and our ideal solution). Because we are starting with a 0 vector, r = b. reshape(-1) reshapes the result as a vector (Numpy thing)
    p[0] = r / np.linalg.norm(r) #p1 = r divided by r_norm  (p1 starts at p[0]) Orthogonalizes?
    
    
    
    for k in range(m_max):
        y = np.asarray(A.dot(p[k])).reshape(-1)
        for j in range(k):
            h[j, k] = np.dot(p[j], y)
            y = y - h[j, k] * p[j]
        R[k + 1, k] = np.linalg.norm(y)
        if (R[k + 1, k] != 0 and k != m_max - 1):
            p[k + 1] = y / R[k + 1, k]
    
        b = np.zeros(m_max + 1)
        b[0] = np.linalg.norm(r)
        
        
        
        result = np.linalg.lstsq(R, b)[0]



    x.append(np.dot(np.asarray(p).transpose(), result) + x0)

    return x





def GMRes(A, b, x0, e, nmax_iter, restart=None):
    r = b - np.asarray(sp.dot(A, x0)).reshape(-1)
    
    x = []
    q = [0] * (nmax_iter)
    
    x.append(r)
    
    q[0] = r / np.linalg.norm(r)
    
    h = np.zeros((nmax_iter + 1, nmax_iter))
    
    for k in range(nmax_iter):
        y = np.asarray(sp.dot(A, q[k])).reshape(-1)
        
        for j in range(k):
            h[j, k] = np.dot(q[j], y)
            y = y - h[j, k] * q[j]
        h[k + 1, k] = np.linalg.norm(y)
        if (h[k + 1, k] != 0 and k != nmax_iter - 1):
            q[k + 1] = y / h[k + 1, k]
    
        b = np.zeros(nmax_iter + 1)
        b[0] = np.linalg.norm(r)
        
        result = np.linalg.lstsq(h, b)[0]
        
    x.append(np.dot(np.asarray(q).transpose(), result) + x0)

return x



























A = np.random.random((5, 5)) #creates random 5x5 matrix
b = np.random.random(5) #creates random solution vector
result = GMRES(A, b)
print(result)



#CHECK

A = np.matrix('1 1; 3 -4')
b = np.array([3, 2])
x0 = np.array([1, 2])
#sp.gmres(A,b,x0)








#####

#### PART 2 -  ####
#A = np.random.random((5, 5)) #creates random 5x5 matrix
#b = np.random.random(5) #creates random solution vector
#x = np.random.random(5) #initial approximation
#e = 10**-6 #input tolerance
#m_max = 50 #Upper bound for number of iteration steps

#GMRES(A,b,x,e,m_max)
#1st iteration
# r = b - A.dot(x) #initial residual
# p = (1/np.linalg.norm(r)
# b = A.dot(p)
# t=np.dot(b.T,r)/np.dot(b.T,b)
# x = x + t*p
# r = r - t*b

#next iterations
# for i in range (2,m_max+1):
#   Beta[i]
# p[i] = r -
