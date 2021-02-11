__global__ void histogram_atomic(char *a, int *result, int N, int BINS, int DIV) {
  // Calculate global thread ID
  int tid = blockIdx.x * blockDim.x + threadIdx.x;

  // Calculate the bin positions where threads are grouped together
  int alpha_position;
  for (int i = tid; i < N; i += (gridDim.x * blockDim.x)) {
    // Calculate the position in the alphabet
    alpha_position = a[i] - 'a';
    atomicAdd(&result[alpha_position / DIV], 1);
  }
}

__global__ void histogram_shared(char *a, int *result, int N, int BINS, int DIV) {
  // Calculate global thread ID
  int tid = blockIdx.x * blockDim.x + threadIdx.x;

  // Allocate a local histogram for each TB
  __shared__ int s_result[BINS_SHARED];

  // Initalize the shared memory to 0
  if (threadIdx.x < BINS) {
    s_result[threadIdx.x] = 0;
  }

  // Wait for shared memory writes to complete
  __syncthreads();

  // Calculate the bin positions locally
  int alpha_position;
  for (int i = tid; i < N; i += (gridDim.x * blockDim.x)) {
    // Calculate the position in the alphabet
    alpha_position = a[i] - 'a';
    atomicAdd(&s_result[(alpha_position / DIV)], 1);
  }

  // Wait for shared memory writes to complete
  __syncthreads();

  // Combine the partial results
  if (threadIdx.x < BINS) {
    atomicAdd(&result[threadIdx.x], s_result[threadIdx.x]);
  }
}
