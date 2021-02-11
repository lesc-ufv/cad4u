#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char const *argv[]) {
  
  int n = 64;
  int a[n][n], b[n][n], c[n][n];
  clock_t time_req;
  
  for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        a[i][j] = i + j;
        b[i][j] = i*2 + j;   
      }
  }
  
  time_req = clock();
  int temp;
  for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
          temp = 0;
          for (int k = 0; k < n; ++k) {
              temp += a[i][k] * b[k][j];
          }
          c[i][j] = temp;   
      }
  } 
  time_req = clock() - time_req;
  
  printf("Multiplication matrix %dx%d\n", n, n);
  printf("Time %.4fs\n", (float)time_req / CLOCKS_PER_SEC);
  return 0;
}