# Matthew Konyndyk
# Math 343 Winter 2017
# Project Assignment: GMRES


# Description: Write tools (library of functions) for operating on sparse matrices, using CSR (compressed sparse row) format (discussed previously and described in an earlier file). More specifically: 1) It should be able to read matrix data from file (the i, j and data entries aij for all non-zero entries of the matrix.) 2) It should be able to perform A times a vector, and AT times a vector. Given A in CSR format generate AT in the same format. This function should use minimal operations (as little as you can think of). Given two matrices A and B in CSR format, compute C = AB and store it also in CSR format.


#Part 1: There should be a test driver that you write, which can:
# 1. Read a matrix A (could be simply the adjacency matrix of a directed or undirected graph).
# 2. Produce B = AT in CSR format.
# 3. Compute C = AB. Check if C is symmetric.


# Part 2: Use some of the functions from your library, for an appropriately given input matrix A, and
# 1. Implement the GMRES algorithm with restart (provided in a separate .pdf file).
# 2. Perform study when you vary mmax = 5, 10, 15, ... the maximal number of steps allowed in the algorithm, and document the total number of iterations and total time to convergence for a given tolerance  (and a given matrix). Write your conclusions from the study.


# Grading:
# We should agree beforehand what kind of test matrices A will be used in the study. You will have to document (describe) the implementation of the library and the GMRES algorithm in a project report. The project report is due no later than March 20 (earlier the better). You need to demonstrate that the code runs (i.e., can generate approximate solution x for various r.h.s. vectors b, sizes of m_max, and tolerance epsilon. The project will be graded after a discussion and looking at your project report on how the library and the GMRES algorithm were implemented.


import csv # https://docs.python.org/2/library/csv.html
import time #https://docs.python.org/2/library/time.html







### FUNCTIONS ###

#creates an nxn sparse matrix. Matrix entry data is filled in at the corresponding i and j locations. All non specified entries are zero.
def assemble_sparse_matrix(i,j,data,size):
    matrix = [[0 for x in range(size)] for y in range(size)] #creates empty array of the proper dimensions
    for x in range (0,len(i)): matrix[i[x]][j[x]] = data[x]
    return matrix

#Displays a nested array matrix properly
def display_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

#writes a sparse row matrix's data to a csv file using i, j, and data lists.
def write_csv(path,i,j,data,mtx_size):
    csv_file = open(path, 'wt')
    writer = csv.writer(csv_file)
    writer.writerow( ('i', 'j', 'data',len(data),mtx_size) ) #len(data) is used for reading
    for x in range(0,len(i)):
        row = [i[x],j[x],data[x]]
        writer.writerow(row)
    csv_file.close()

#loads the i, j, and data vectors from a sparse rom matrix.
def load_csv(path):
    csv_file = open(path, 'rt')
    reader = csv.reader(csv_file)
    array = reader.next() #first line is header info
    num_entries = int(array[3])
    mtx_size = int(array[4])
    x = 0
    while num_entries > 0:
        array = reader.next()
        i[x] = int(array[0])
        j[x] = int(array[1])
        data[x] = int(array[2])
        num_entries -= 1
        x+=1
    csv_file.close()
    return i,j,data,mtx_size

#performs the multiplication of two nested row matrices.
def matrix_mult(A,B):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in B]))






#### PART 1 - Basic Matrix Operations ####

# setup

size = 8
i = [0, 3, 5, 6, 7] #
j = [1, 2, 4, 5, 6]
data = [7, 7, 7, 7, 7]
path = 'MTX_A.csv'

# - Read Matrix A
write_csv(path,i,j,data,size) #writes the information we just described to a csv file
i,j,data,mtx_size = load_csv(path) #loads the csv file we created
mtx_A = assemble_sparse_matrix(i,j,data,size) #creates a sparse matrix from i, j, data vectors
display_matrix(mtx_A) #displays the matrix

# - Perform A times a vector

# - Perform AT times a vector

# - Geven A in CSR format generate AT in the same format using minimum operations

# - Given two matrices A and B in CSR format, compute C = AB and store it also in CSR format.

# - Produce B = AT in CSR format.

# - Compute C = AB. Check if C is symmetric.







#### PART 2 -  ####



