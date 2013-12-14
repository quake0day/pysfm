#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import numpy as np
from numpy import lialg as la
from pycuda import driver, compiler, gpuarray, tools

# -- initialize the device
import pycuda.autoinit

kernel_code_template = """
__global__ void MatrixMulKernel(float *A, float *B, float *C)
{
	const uint
}
