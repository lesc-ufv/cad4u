// Verify the result on the CPU
void verify_result(int *array, int *mask, int *result, int n, int MASK_LENGTH) {
  int radius = MASK_LENGTH / 2;
  int temp;
  int start;
  for (int i = 0; i < n; i++) {
    start = i - radius;
    temp = 0;
    for (int j = 0; j < MASK_LENGTH; j++) {
      if ((start + j >= 0) && (start + j < n)) {
        temp += array[start + j] * mask[j];
      }
    }
    assert(temp == result[i]);
  }
}
