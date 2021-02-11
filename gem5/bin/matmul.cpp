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
  
  printf("Multiplication matrix %dx%d\n", n, n);
  return 0;
}