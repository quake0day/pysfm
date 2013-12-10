from mpi4py import MPI

def pprint(string, comm=MPI.COMM_WORLD):
    if comm.rank == 0:
        print(string)