__global__ void convolution_1d_naive(int *array, int *mask, int *result, int n, int MASK_LENGTH) {
  // Global thread ID calculation
  int tid = blockIdx.x * blockDim.x + threadIdx.x;

  // Calculate radius of the mask
  int r = MASK_LENGTH / 2;

  // Calculate the starting point for the element
  int start = tid - r;

  // Temp value for calculation
  int temp = 0;

  // Go over each element of the mask
  for (int j = 0; j < MASK_LENGTH; j++) {
    // Ignore elements that hang off (0s don't contribute)
    if (((start + j) >= 0) && (start + j < n)) {
      // accumulate partial results
      temp += array[start + j] * mask[j];
    }
  }

  // Write-back the results
  result[tid] = temp;
}

__global__ void convolution_1d_tiled(int *array, int *mask, int *result, int n, int MASK_LENGTH) {
  // Global thread ID calculation
  int tid = blockIdx.x * blockDim.x + threadIdx.x;

  // Store all elements needed to compute output in shared memory
  extern __shared__ int s_array[];

  // r: The number of padded elements on either side
  int r = MASK_LENGTH / 2;

  // d: The total number of padded elements
  int d = 2 * r;

  // Size of the padded shared memory array
  int n_padded = blockDim.x + d;

  // Offset for the second set of loads in shared memory
  int offset = threadIdx.x + blockDim.x;

  // Global offset for the array in DRAM
  int g_offset = blockDim.x * blockIdx.x + offset;

  // Load the lower elements first starting at the halo
  // This ensure divergence only once
  s_array[threadIdx.x] = array[tid];

  // Load in the remaining upper elements
  if (offset < n_padded) {
    s_array[offset] = array[g_offset];
  }
  __syncthreads();

  // Temp value for calculation
  int temp = 0;

  // Go over each element of the mask
  for (int j = 0; j < MASK_LENGTH; j++) {
    temp += s_array[threadIdx.x + j] * mask[j];
  }

  // Write-back the results
  result[tid] = temp;
}
