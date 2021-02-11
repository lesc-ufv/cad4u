void initDataRandom(float *a, int size){
  srand(time(NULL));
  for(int i = 0; i < size; ++i) a[i] = 1.0 * (rand() % 5);
}
