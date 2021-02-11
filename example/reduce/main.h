#define SHMEM_SIZE 256 * 4   // memory shared

#include <sys/time.h>
#include <cuda_runtime.h>
#include <stdio.h>
#include <fstream>

#include "kernel.h"
#include "time_analisys.h"

int main(int argc, char **argv){
    // set up device
    cudaDeviceProp deviceProp;
    cudaGetDeviceProperties(&deviceProp, 0);
    printf("device %d: %s \n", 0, deviceProp.name);
    cudaSetDevice(0);
    int size = (1 << 28); 
    
    ofstream myfile;
	myfile.open ("results_reduce.csv");
	myfile << "threads, Neighbored, Shared, Unrolling8\n";

	for (int j = 0; j < n_threads.size(); ++j) {

		// total number of elements to reduce
		myfile << n_threads[j] << ",";

		// execution configuration
		int blocksize = n_threads[j];   // initial block size

		dim3 block (blocksize, 1);
		dim3 grid  ((size + block.x - 1) / block.x, 1);

		// allocate host memory
		size_t bytes = size * sizeof(int);
		int *h_idata = (int *) malloc(bytes);
		int *h_odata = (int *) malloc(grid.x * sizeof(int));
		int *tmp     = (int *) malloc(bytes);
		
		printf("Nº threads: %d\n", n_threads[j]);
		printf("Tamanho do vetor: %d \n", size);
		printf("Espaço ocupado do vetor em bytes: %d \n", bytes);

		//printf("Blocks: %d\nThreads/blocks: %d\nThreads(total): %d\n\n", grid.x, block.x, grid.x*block.x);
		
		// initialize the array 
		for (int i = 0; i < size; i++){
		    h_idata[i] = (int)( rand() & 0xFF ); // mask off high 2 bytes to force max number to 255
		}

		memcpy(tmp, h_idata, bytes);
		
		float start;
		int gpu_sum = 0;

		// allocate device memory
		int *d_idata = NULL;
		int *d_odata = NULL;
		cudaMalloc((void **) &d_idata, bytes);
		cudaMalloc((void **) &d_odata, grid.x * sizeof(int));

		// cpu reduction
		//start = clock();
		//int cpu_sum = recursiveReduce (tmp, size);
		//start = clock() - start;
		//float time_cpu = 1000*((float)start) / CLOCKS_PER_SEC;
		//printf("Time CPU reduce:            %6.2f ms\n", time_cpu, cpu_sum);
		//myfile << time_cpu << ",";

		//# kernel 1: reduceNeighbored
		cudaMemcpy(d_idata, h_idata, bytes, cudaMemcpyHostToDevice);
		
		time_start();
		reduceNeighbored<<<grid, block>>>(d_idata, d_odata, size);
		cudaDeviceSynchronize();
		time_end();

		printf("Time GPU reduce Neighbored: %6.2lf ms\n", elapsed_time);
		
		myfile << elapsed_time << ",";

		cudaMemcpy(h_odata, d_odata, grid.x * sizeof(int), cudaMemcpyDeviceToHost);
		gpu_sum = 0;

		for (int i = 0; i < grid.x; i++) gpu_sum += h_odata[i];

		//if(gpu_sum != cpu_sum) printf("Test failed! Value CPU is %d and GPU is %d\n", cpu_sum, gpu_sum);

		//# kernel 1: reduce shared
		cudaMemcpy(d_idata, h_idata, bytes, cudaMemcpyHostToDevice);
		
		time_start();
		reduceShared<<<grid, block>>>(d_idata, d_odata, size);
		cudaDeviceSynchronize();
		time_end();

		printf("Time GPU reduce Shared:    %7.2lf ms\n", elapsed_time);
		
		myfile << elapsed_time << ",";

		cudaMemcpy(h_odata, d_odata, grid.x * sizeof(int), cudaMemcpyDeviceToHost);
		gpu_sum = 0;

		for (int i = 0; i < grid.x; i++) gpu_sum += h_odata[i];

		//if(gpu_sum != cpu_sum) printf("Test failed! Value CPU is %d and GPU is %d\n", cpu_sum, gpu_sum);

		//# kernel 6: reduceUnrolling8
		cudaMemcpy(d_idata, h_idata, bytes, cudaMemcpyHostToDevice);
		
		time_start();
		reduceUnrolling8<<<grid.x / 8, block>>>(d_idata, d_odata, size);
		cudaDeviceSynchronize();
		time_end();
		printf("Time GPU reduce Unrolling: %7.2lf ms\n\n", elapsed_time);
		
		myfile << elapsed_time << "\n";
		
		cudaMemcpy(h_odata, d_odata, grid.x / 8 * sizeof(int), cudaMemcpyDeviceToHost);
		gpu_sum = 0;
		for (int i = 0; i < grid.x / 8; i++) gpu_sum += h_odata[i];

		// free host memory
		free(h_idata);
		free(h_odata);

		// free device memory
		cudaFree(d_idata);
		cudaFree(d_odata);

		// reset device
		cudaDeviceReset();

		//if(gpu_sum != cpu_sum) printf("Test failed! Value CPU is %d and GPU is %d\n", cpu_sum, gpu_sum);
	}
	myfile.close();

    return EXIT_SUCCESS;
}
