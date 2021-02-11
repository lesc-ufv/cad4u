#include <sys/time.h>
#include <cuda_runtime.h>
#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>

__constant__ int CONST_MASK[1000];

#include "kernel.h"
#include "verify_convolution.h"
#include "time_analisys.h"

int main() {

  cudaDeviceProp deviceProp;
  cudaGetDeviceProperties(&deviceProp, 0);
  cudaSetDevice(0);
  printf("device %d: %s \n", 0, deviceProp.name);
  
  clock_t t_start; 
  
  ofstream myfile;
  myfile.open ("results_conv.csv");
  myfile << "mask, Naive , Tiled\n";
  
  int VECTOR_LENGTH = (1 << 28);
  printf("Tamanho em bytes do vetor: %d\n", VECTOR_LENGTH * sizeof(int));
  
  for (int k = 0; k < data_mask.size(); ++k) {

	  int MASK_LENGTH = data_mask[k];

	  myfile << MASK_LENGTH << ",";

	  int n = VECTOR_LENGTH;
	  int r = MASK_LENGTH / 2;

	  int bytes_n = n * sizeof(int);
	  int bytes_m = MASK_LENGTH * sizeof(int);

	  std::vector<int> h_array(n);

	  // ... and initialize it
	  std::generate(begin(h_array), end(h_array), [](){ return rand() % 100; });

	  // Allocate the mask and initialize it
	  int *h_mask = new int[MASK_LENGTH];
	  for (int i = 0; i < MASK_LENGTH; i++) { h_mask[i] = rand() % 10; }

	  // Allocate space for the result
	  std::vector<int> h_result(n);
	  std::vector<int> h_result2(n);

	  // Allocate space on the device
	  int *d_array, *d_mask, *d_result, *d_result2;
	  cudaMalloc(&d_array, bytes_n);
	  cudaMalloc(&d_mask, bytes_m);
	  cudaMalloc(&d_result, bytes_n);
	  cudaMalloc(&d_result2, bytes_n);

	  // Copy the data to the device
	  cudaMemcpy(d_array, h_array.data(), bytes_n, cudaMemcpyHostToDevice);
	  cudaMemcpy(d_mask, h_mask, bytes_m, cudaMemcpyHostToDevice);

	  // Threads per TB
	  int THREADS = 512;

	  // Number of TBs
	  int BLOCKS = (n + THREADS - 1) / THREADS;

	  //printf("Blocks: %d\nThreads/blocks: %d\nThreads(total): %d\n\n", BLOCKS, THREADS, THREADS*BLOCKS);

	  time_start();
	  //# Call the kernel naive
	  convolution_1d_naive<<<BLOCKS, THREADS>>>(d_array, d_mask, d_result, n, MASK_LENGTH);
	  cudaDeviceSynchronize();
	  //#-----------------------
	  time_end();

	  cudaMemcpy(h_result.data(), d_result, bytes_n, cudaMemcpyDeviceToHost);

	  float time_gpu_naive = 1000 * ((float)(clock() - t_start)) / CLOCKS_PER_SEC;

	  //verify_result(h_array.data(), h_mask, h_result.data(), n, MASK_LENGTH); // Verify the result

	  size_t SHMEM = (THREADS + r*2) * sizeof(int);

	  //printf("Blocks: %d\nThreads/blocks: %d\nThreads(total): %d\nMSHARED: %d\n\n", BLOCKS, THREADS, THREADS*BLOCKS, SHMEM);

	  printf("Time GPU naive: %.2lf ms\n", elapsed_time);
	  myfile << elapsed_time << ",";

	  time_start(); 
	  //# Call the kernel tiled
	  convolution_1d_tiled<<<BLOCKS, THREADS, SHMEM>>>(d_array, d_mask, d_result2, n, MASK_LENGTH);
	  cudaDeviceSynchronize();
	  //#-----------------------
	  time_end();
	  printf("Time GPU tiled: %.2lf ms\n", elapsed_time);
	  myfile << elapsed_time << "\n";

	  cudaMemcpy(h_result2.data(), d_result2, bytes_n, cudaMemcpyDeviceToHost);

	  float time_gpu_tiled = 1000 * ((float)(clock() - t_start)) / CLOCKS_PER_SEC;

	  //verify_result(h_array.data(), h_mask, h_result2.data(), n, MASK_LENGTH); // Verify the result

	  // Free allocated memory on the device and host
	  cudaFree(d_result); cudaFree(d_result2); cudaFree(d_mask); cudaFree(d_array);
  }
  myfile.close();

  return 0;
}
