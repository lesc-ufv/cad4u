
const int SHMEM_SIZE = 4096;

#include "include.h"
#include <fstream>

int main(int argc, char* argv[]) { 

    cudaDeviceProp deviceProp;
    cudaGetDeviceProperties(&deviceProp, 0);
    printf("device %d: %s \n", 0, deviceProp.name);
    cudaSetDevice(0);

	ofstream myfile;
	myfile.open ("results_matrix.csv");
	myfile << "size, Naive ,Tiled\n";
	
	for (int i = 0; i < data.size(); ++i) {
	
		int N = data[i];

		myfile << N << ",";

		size_t bytes = N * N * sizeof(float);

		printf("Ocupação tamanho da Matriz %ld\n", bytes);
		
		//float *h_cpu;
		float *h_a, *h_b, *h_naive, *h_tiled;
		float *d_a, *d_b, *d_naive, *d_tiled;
		//float time_cpu;

		h_a = (float*) malloc(bytes);
		h_b = (float*) malloc(bytes);
		//h_cpu = (float*) malloc(bytes);
		h_naive = (float*) malloc(bytes);
		h_tiled = (float*) malloc(bytes);

		initDataRandom(h_a, N*N);
		initDataRandom(h_b, N*N);
		//memset(h_cpu, 0, bytes);
		memset(h_naive, 0, bytes);
		memset(h_tiled, 0, bytes);

		cudaMalloc(&d_a, bytes);
		cudaMalloc(&d_b, bytes);
		cudaMalloc(&d_naive, bytes);
		cudaMalloc(&d_tiled, bytes);

		// Copy data to the device
		cudaMemcpy(d_a, h_a, bytes, cudaMemcpyHostToDevice);
		cudaMemcpy(d_b, h_b, bytes, cudaMemcpyHostToDevice);
		cudaMemcpy(d_naive, h_naive, bytes, cudaMemcpyHostToDevice);
		cudaMemcpy(d_tiled, h_tiled, bytes, cudaMemcpyHostToDevice);

		// cpu execution
		//time_clock = clock(); 
		//cpu_mmatrix(h_cpu, h_a, h_b, N);
		//time_clock = clock() - time_clock;
		//time_cpu = 1000*((float)time_clock) / CLOCKS_PER_SEC;

		// Threads per CTA dimension
		int THREADS = 32;

		// Blocks per grid dimension (assumes THREADS divides N evenly)
		int BLOCKS = N / THREADS;

		// Use dim3 structs for block  and grid dimensions
		dim3 threads(THREADS, THREADS);
		dim3 blocks(BLOCKS, BLOCKS);

		//printf("Blocks: %d\nThreads/blocks: %d\nThreads(total): %d\n\n", BLOCKS, THREADS, THREADS*BLOCKS);

		//printf("Time cpu:       %.2lf ms\n", time_cpu);

		printf("Size: %dx%d\n", N, N);

		//# Launch kernel Naive
		time_start();
		matrixMul_naive<<<blocks, threads>>>(d_naive, d_a, d_b, N);
		cudaDeviceSynchronize();
		time_end();
		
		cudaMemcpy(h_naive, d_naive, bytes, cudaMemcpyDeviceToHost);
		printf("Time GPU naive: %7.2lf ms\n", elapsed_time);
		myfile << elapsed_time << ",";

		//# Launch kernel Tiled
		time_start();
		matrixMul_tiled<<<blocks, threads>>>(d_tiled, d_a, d_b, N);
		cudaDeviceSynchronize();
		time_end();
		
		cudaMemcpy(h_tiled, d_tiled, bytes, cudaMemcpyDeviceToHost);
		printf("Time GPU tiled: %7.2lf ms\n\n", elapsed_time);
		myfile << elapsed_time << "\n";

		//checkResults(h_cpu, h_naive, N*N);
		//checkResults(h_cpu, h_tiled, N*N);
		
		//free(h_cpu);
		free(h_tiled); free(h_naive); free(h_a); free(h_b); 
    	cudaFree(d_naive); cudaFree(d_tiled); cudaFree(d_a); cudaFree(d_b); 
	}
	myfile.close();
	
    return 0;
}

