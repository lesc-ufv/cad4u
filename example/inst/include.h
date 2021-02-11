void checkElementsAre(float target, float *vector, int N) {
  for(int i = 0; i < N; i++) {
    if(vector[i] != target) {
      printf("FAIL: vector[%d] - %0.0f does not equal %0.0f\n", i, vector[i], target);
      exit(1);
    }
  }
  printf("Success! All values calculated correctly.\n");
}

// inicializa os dados
void initWith(float num, float *a, int N) {
  for(int i = 0; i < N; ++i) {
    a[i] = num;
  }
}

__global__
void addVectorsInto(float *result, float *a, float *b, int N){
  int index = threadIdx.x + blockIdx.x * blockDim.x;
  int stride = blockDim.x * gridDim.x;

  for(int i = index; i < N; i += stride)
    result[i] = a[i] + b[i];
}
