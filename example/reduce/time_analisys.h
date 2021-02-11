
float elapsed_time;
cudaEvent_t start, stop;                             //# Declara dois eventos

void time_start(){
  cudaEventCreate(&start);                          //# Irá marcar o inicio da execucao
  cudaEventCreate(&stop);                           //# Irá  marcar o final da execucao
  cudaEventRecord(start, 0);                        //# insere na fila 
}

void time_end() {
  cudaEventRecord(stop, 0);                          //# insere na fila
  cudaEventSynchronize(stop);                        //# espera terminar
  cudaEventElapsedTime(&elapsed_time, start, stop);  //# calcula
}
