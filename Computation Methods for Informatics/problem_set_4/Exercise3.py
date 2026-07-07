import matplotlib.pyplot as plt
import numpy
import time
from mpi4py import MPI

xlo = -2.5
ylo = -1.5
yhi = 1.5
xhi = 0.75
nx = 2048
ny = 1536
dx = (xhi - xlo) / nx
dy = (yhi - ylo) / ny

iter_limit = 200
set_threshold = 2

def mandelbrot_test(x, y):
    z = 0
    c = x + y * 1j
    for i in range(iter_limit):
        z = z ** 2 + c
        if abs(z) > set_threshold:
            return i
    return i

def calculate_set(start_row, end_row):
    rows = end_row - start_row
    result = numpy.zeros([rows, nx])
    for i in range(rows):
        y = (start_row + i) * dy + ylo
        for j in range(nx):
            x = j * dx + xlo
            result[i, j] = mandelbrot_test(x, y)
    return result

if __name__ == "__main__":
    communicator = MPI.COMM_WORLD
    rank = communicator.rank
    processors = communicator.size

    rows_per_processor = ny // processors
    start_row = rank*rows_per_processor
    if rank == processors - 1:
        end_row = ny
    else:
        end_row = start_row + rows_per_processor
    
    start_time = time.perf_counter()
    
    processor_result = calculate_set(start_row, end_row)
    mandelbrot_set = numpy.zeros([ny,nx])
    communicator.Allgather(processor_result, mandelbrot_set)

    stop_time = time.perf_counter()

    if(rank == 0):
        print(f"Calculation took {stop_time - start_time} seconds")
        plt.imshow(mandelbrot_set, interpolation="nearest", cmap="Greys")
        plt.gca().set_aspect("equal")
        plt.axis("off")
        plt.title(f"Mandelbrot Set with {processors} Processor(s)")
        plt.show()