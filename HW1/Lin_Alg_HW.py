# Matthew Konyndyk
# Applied Linear Algebra
# Last update: 3/5/2017

#This program reads a CSR file in i,j,data format, prints the matrix to the console in decoded sparse row form.



import csv # https://docs.python.org/2/library/csv.html
import time #https://docs.python.org/2/library/time.html



import numpy as np


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






#### MAIN ####


# Matrix storage handled with native python libraries

size = 8
i = [0, 3, 5, 6, 7] #
j = [1, 2, 4, 5, 6]
data = [7, 7, 7, 7, 7]
path = 'test.csv'

i,j,data,mtx_size = load_csv(path)
mtx = assemble_sparse_matrix(i,j,data,size) #creates a sparse matrix from i, j, data vectors
display_matrix(mtx) #displays the matrix
write_csv(path,i,j,data,size)


# Matrix operations handled with numpy

A = np.matrix(mtx) # converts the matrix to numpy format
vector = np.random.rand(size) # creates a vector of random values
result = np.dot(A,vector)
print(result)








