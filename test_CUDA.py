import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy
import time

n = 4
a = numpy.float32(numpy.random.randn(n,n))
b = numpy.float32(numpy.random.randn(n,n))
for i in range(n):
	for j in range(n):
		a[i,j] = i+j
		b[i,j] = i+j
tic = time.time()
axb = a*b
print a
print b
print "===="
print numpy.dot(a,b)
toc = time.time() - tic
print toc, "s for CPU"

tic = time.time()
a_gpu = gpuarray.to_gpu(a)
b_gpu = gpuarray.to_gpu(b)
axbGPU = gpuarray.dot(a_gpu,b_gpu)

print "===="
print axbGPU
toc=time.time()-tic
print toc,"s for GPU"