# Matthew Konyndyk
# Math 343 Winter 2017
# Final Project Part 1


# Description: Write tools (library of functions) for operating on sparse matrices, using CSR (compressed sparse row) format (discussed previously and described in an earlier file). More specifically: 1) It should be able to read matrix data from file (the i, j and data entries aij for all non-zero entries of the matrix.) 2) It should be able to perform A times a vector, and AT times a vector. Given A in CSR format generate AT in the same format. This function should use minimal operations (as little as you can think of). Given two matrices A and B in CSR format, compute C = AB and store it also in CSR format.


#Part 1: There should be a test driver that you write, which can:
# 1. Read a matrix A (could be simply the adjacency matrix of a directed or undirected graph).
# 2. Produce B = AT in CSR format.
# 3. Compute C = AB. Check if C is symmetric.



import csv # https://docs.python.org/2/library/csv.html
import numpy as np



### FUNCTIONS ###

#creates an nxn sparse matrix. Matrix entry data is filled in at the corresponding i (row) and j (vector) locations. All non specified entries are zero.
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

#loads the i, j, and data vectors from a sparse row matrix.
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

#Transposes a matrix
def transpose(mtx):
    mtxT = map(list, zip(*mtx))
    return mtxT

#input is a nested list matrix, output is the CSR vectors
def return_data_vectors(mtx):
    size = (len(mtx))
    data = [num for num in [item for sublist in mtx for item in sublist] if num] # flattens the nested matrix to a list, then extracts only the non zero entries
    i = np.nonzero(mtx)[0]
    j = np.nonzero(mtx)[1]
    print(i,j,data,size)
    return i,j,data,size

def symmetric_check(mtx):
    return (mtx.transpose() == mtx).all()



# SETUP

# matrix A
i,j,data,size = [0, 3, 5, 6, 7],[1, 2, 4, 5, 6],[7, 7, 7, 7, 7],8
write_csv('MTX_A.csv',i,j,data,size) #writes to csv file
i,j,data,mtx_size = load_csv('MTX_A.csv')
A = assemble_sparse_matrix(i,j,data,size) #creates a sparse matrix from i, j, data vectors
# matrix B
i,j,data,size = [2, 3, 4, 6, 6],[1, 2, 1, 5, 6],[8, 8, 8, 8, 8],8
write_csv('MTX_B.csv',i,j,data,size) #writes to csv file
i,j,data,mtx_size = load_csv('MTX_B.csv')
B = assemble_sparse_matrix(i,j,data,size) #creates a sparse matrix from i, j, data vectors





#### PART 1 - Basic Matrix Operations ####

# - Read Matrix A
display_matrix(A) #displays the matrix

# - Perform A times a vector
v = [1, 1, 1, 1, 1, 1, 1, 1]
result = np.dot(A,v)
print result

# - Perform AT times a vector
AT = transpose(A)
result = np.dot(AT,v)
print result

# - Geven A in CSR format generate AT in the same format using minimum operations
display_matrix(AT)

# - Given two matrices A and B in CSR format, compute C = AB and store it also in CSR format.
C = np.dot(A,B)
i,j,data,size = return_data_vectors(C)
write_csv('MTX_C.csv',i,j,data,size) #writes the information to a csv file

# - Produce B = AT in CSR format.
B = transpose(A)
#show B in CSR format
i,j,data,size = return_data_vectors(B)
write_csv('MTX_B.csv',i,j,data,size)

# - Compute C = AB. Check if C is symmetric.
C = np.dot(A,B)
print C
print 'Matrix Symmetry: ',symmetric_check(C)


