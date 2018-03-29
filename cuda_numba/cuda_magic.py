
import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(['float32(float32, float32)'], target='cuda')
def pow_cuda(a, b):
    return a ** b

def pow_serial(a, b):
    return a ** b

def main(use_cuda):
    vec_size = 10000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    if use_cuda: c = pow_cuda(a, b)
    else: pow_serial(a, b)
    duration = timer() - start

    print(duration)

if __name__ == '__main__':
    print("Without CUDA: ", end="")
    main(False)

    print("With CUDA: ", end="")
    main(True)
