#include <sys/time.h>
#include <cuda_runtime.h>
#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <fstream>

using namespace std;

//# VARIAVEIS
#define PROBLEM_SIZE 1 << 26
#define BINS_SHARED 1024

#include "kernel.h"
#include "time_analisys.h"

int main() {
    
  cudaDeviceProp deviceProp;
  cudaGetDeviceProperties(&deviceProp, 0);
  cudaSetDevice(0);
  printf("device %d: %s \n", 0, deviceProp.name);
  
  ofstream myfile;
  ofstream f;
  myfile.open ("results_hist.csv");
  myfile << "bins, atomic, shared\n";

  for (int j = 0; j < data_bin.size(); ++j) {
  
  	  int BINS = data_bin[j];
  	  
  	  myfile << BINS << ",";
  	  
  	  int DIV = ((26 + BINS - 1) / BINS);

	  // Declare our problem size
	  int N = PROBLEM_SIZE; 

	  // Allocate memory on the host
	  vector<char> h_input(N);
	  vector<int> h_result(BINS);
	  vector<int> h_result_shared(BINS);
	  
	  // Initialize the array
	  srand(1);
	  generate(begin(h_input), end(h_input), []() { return 'a' + (rand() % 26); });

	  // Allocate memory on the device
	  char *d_input;
	  int *d_result, *d_result_shared;
	  cudaMalloc(&d_input, N);
	  cudaMalloc(&d_result, BINS * sizeof(int));
	  cudaMalloc(&d_result_shared, BINS * sizeof(int));

	  // Copy the array to the device
	  cudaMemcpy(d_input, h_input.data(), N, cudaMemcpyHostToDevice);
	  cudaMemcpy(d_result, h_result.data(), BINS * sizeof(int), cudaMemcpyHostToDevice);
	  cudaMemcpy(d_result_shared, h_result_shared.data(), BINS * sizeof(int), cudaMemcpyHostToDevice);

	  // Number of threads per threadblock
	  int THREADS = 32;

	  // Calculate the number of threadblocks
	  int BLOCKS = N / THREADS;

	  //printf("Blocks: %d\nThreads/blocks: %d\nThreads(total): %d\n\n", BLOCKS, THREADS, THREADS*BLOCKS);

	  time_start();
	  //#---------- Launch the kernel atomic
	  histogram_atomic<<<BLOCKS, THREADS>>>(d_input, d_result, N, BINS, DIV);
	  cudaDeviceSynchronize();
	  //#----------------------------
	  time_end();
	  printf("Time GPU atomic: %.2lf ms\n", elapsed_time);
	  myfile << elapsed_time << ",";

	  cudaMemcpy(h_result.data(), d_result, BINS * sizeof(int), cudaMemcpyDeviceToHost);

	  time_start();
	  //#----------- Launch the kernel shared
	  histogram_shared<<<BLOCKS, THREADS>>>(d_input, d_result_shared, N, BINS, DIV);
	  cudaDeviceSynchronize();
	  //#----------------------------
	  time_end();
	  printf("Time GPU shared: %.2lf ms\n", elapsed_time);
	  myfile << elapsed_time << "\n";

	  cudaMemcpy(h_result_shared.data(), d_result, BINS * sizeof(int), cudaMemcpyDeviceToHost);

	  // Functional test (the sum of all bins == N)
	  assert(N == accumulate(begin(h_result), end(h_result), 0));
	  
	  f.open ("histogram_"+ to_string(data_bin[j]) +".txt");
	  printf("\nHistogram\n");
	  for (int i = 0; i < BINS; ++i) {
	  	  f << i << " " << h_result[i] << "\n";
		  printf("%d: %d\n", i, h_result[i]);
	  }
	  printf("\n");
	  f.close();

	  // Free memory
	  cudaFree(d_input); cudaFree(d_result); cudaFree(d_result_shared);
  }

  return 0;
}
