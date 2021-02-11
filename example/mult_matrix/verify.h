void checkResults(float *cpu, float *gpu, int size){
  bool pass = true;
  for(int i = 0; i < size; ++i){
    if(abs(cpu[i] - gpu[i]) > 0.001){
      printf("FAIL: value of position (%d,%d) on cpu %.2f != %.2f on gpu\n", i/size, i%size, cpu[i], gpu[i]); pass = false; break;
    }
  }
  if (pass) printf("Sucesso! todos os valores foram calculados corretamente!\n");
}
