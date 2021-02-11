void cpu_mmatrix(float *hres, float *a, float *b, int n){
    float temp;
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < n; ++j){
            temp = 0.0;
            for (int k = 0; k < n; ++k) {
                temp += a[i*n+k] * b[k*n+j];
            }
            hres[i*n+j] = temp;
        }
    }
}

__global__ void matrixMul_naive(float *c, float *a, float *b, int n) {
  // Compute each thread's global row and column index
  int row = blockIdx.y * blockDim.y + threadIdx.y;
  int col = blockIdx.x * blockDim.x + threadIdx.x;

  // Iterate over row, and down column
  c[row * n + col] = 0;
  for (int k = 0; k < n; k++) {
    // Accumulate results for a single element
    c[row * n + col] += a[row * n + k] * b[k * n + col];
  }
}

__global__ void matrixMul_tiled(float *c, float *a, float *b, int n) {
  // Compute each thread's global row and column index
  int row = blockIdx.y * blockDim.y + threadIdx.y;
  int col = blockIdx.x * blockDim.x + threadIdx.x;

  // Statically allocated shared memory
  __shared__ int s_a[SHMEM_SIZE];
  __shared__ int s_b[SHMEM_SIZE];

  // Accumulate in temporary variable
  int tmp = 0;

  // Sweep tile across matrix
  for (int i = 0; i < n; i += blockDim.x) {
    // Load in elements for this tile
    s_a[threadIdx.y * blockDim.x + threadIdx.x] = a[row * n + i + threadIdx.x];
    s_b[threadIdx.y * blockDim.x + threadIdx.x] = b[i * n + threadIdx.y * n + col];

    // Wait for both tiles to be loaded in before doing computation
    __syncthreads();

    // Do matrix multiplication on the small matrix
    for (int j = 0; j < blockDim.x; j++) {
      tmp += s_a[threadIdx.y * blockDim.x + j] * s_b[j * blockDim.x + threadIdx.x];
    }

    // Wait for all threads to finish using current tiles before loading in new ones
    __syncthreads();
  }

  // Write back results
  c[row * n + col] = tmp;
}
