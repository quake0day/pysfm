from mpi4py import MPI
import numpy
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size
rank = comm.Get_rank
print size
print rank

def matvec(comm, A, x):
    m = A.shape[0] # local rows
    p = comm.Get_size()
    xg = numpy.zeros(m*p, dtype='d')
    comm.Allgather([x,  MPI.DOUBLE],
                   [xg, MPI.DOUBLE])
    y = numpy.dot(A, xg)
    return y

A = np.array([[ 2.  ,  0.  , -0.5 ],[ 0.05,  3.  ,  0.1 ],[ 0.  ,  0.  ,  1.  ]])
x = np.array([ 0.0782,  0.0345,  0.3304])
y = matvec(comm, A, x)
print y