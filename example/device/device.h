#include <stdio.h>
 
int getSPcores(cudaDeviceProp devProp){  
    int cores = 0;
    int mp = devProp.multiProcessorCount;
    switch (devProp.major){
     case 2: // Fermi
      if (devProp.minor == 1) cores = mp * 48; else cores = mp * 32; break;
     case 3: // Kepler
      cores = mp * 192; break;
     case 5: // Maxwell
      cores = mp * 128; break;
     case 6: // Pascal
      if ((devProp.minor == 1) || (devProp.minor == 2)) cores = mp * 128; else if (devProp.minor == 0) cores = mp * 64; else printf("Unknown device type\n"); break;
     case 7: // Volta and Turing
      if ((devProp.minor == 0) || (devProp.minor == 5)) cores = mp * 64; else printf("Unknown device type\n"); break;
     case 8: // Ampere
      if (devProp.minor == 0) cores = mp * 64; else printf("Unknown device type\n"); break;
     default:
      printf("Unknown device type\n"); break;
    }
    return cores;
}

// Print device properties
void printDevProp(cudaDeviceProp devProp){
    printf("Name:                                          %s\n", devProp.name);
    printf("CUDA Capability Major/Minor version number:    %d.%d\n", devProp.major, devProp.minor);
    printf("Total amount of global memory:                 %.1f MB (%u bytes)\n", devProp.totalGlobalMem / 1048576.0, devProp.totalGlobalMem);
    printf("Number of multiprocessors:                     %d\n", devProp.multiProcessorCount);
    printf("CUDA Cores per multiprocessors:                %d\n", getSPcores(devProp)/devProp.multiProcessorCount);
    printf("CUDA Cores:                                    %d\n", getSPcores(devProp));
    printf("Register per multiprocessors:                  %d\n", devProp.regsPerMultiprocessor);
    printf("GPU Max Clock Rate:                            %.1f MHz (%.2f GHz)\n", devProp.clockRate/1000.0, devProp.clockRate/1000000.0);
    printf("Memory Clock Rate:                             %.1f MHz\n", devProp.memoryClockRate / 1000.0);
    printf("Memory Bus Width:                              %d bit\n", devProp.memoryBusWidth);
    printf("L2 Cache Size:                                 %.1f MB (%d bytes)\n", devProp.l2CacheSize/1048576.0, devProp.l2CacheSize);
    printf("Maximum Texture Dimension Size (x,y,z):        1D=(%d), 2D(%d, %d), 3D(%d, %d, %d)\n", devProp.maxTexture1D, devProp.maxTexture2D[0], devProp.maxTexture2D[1], devProp.maxTexture3D[0], devProp.maxTexture3D[1], devProp.maxTexture3D[2]);
    printf("Maximum Layered 1D Texture Size, (num) layers: 1D=(%d), %d layers\n", devProp.maxTexture1DLayered[0], devProp.maxTexture1DLayered[1]);
    printf("Maximum Layered 2D Texture Size, (num) layers  2D=(%d, %d), %d layers\n", devProp.maxTexture2DLayered[0], devProp.maxTexture2DLayered[1], devProp.maxTexture2DLayered[2]);
    printf("Total amount of constant memory:               %u\n", devProp.totalConstMem);
    printf("Total amount of shared memory per block:       %.0f KB (%u bytes)\n", devProp.sharedMemPerBlock / 1024.0, devProp.sharedMemPerBlock);
    printf("Total shared memory per multiprocessor:        %.0f KB (%d bytes)\n", devProp.sharedMemPerMultiprocessor/1024.0, devProp.sharedMemPerMultiprocessor);
    printf("Total number of registers available per block: %d\n", devProp.regsPerBlock);
    printf("Warp size:                                     %d\n", devProp.warpSize);
    printf("Maximum number of threads per multiprocessor:  %d\n", devProp.maxThreadsPerMultiProcessor);
    printf("Maximum number of threads per block:           %d\n", devProp.maxThreadsPerBlock);
    printf("Max dimension size of a thread block (x,y,z):  (%d, %d, %d)\n", devProp.maxThreadsDim[0], devProp.maxThreadsDim[1], devProp.maxThreadsDim[2]);
    printf("Max dimension size of a grid size    (x,y,z):  (%d, %d, %d)\n", devProp.maxGridSize[0], devProp.maxGridSize[1], devProp.maxGridSize[2]);
    printf("Maximum memory pitch:                          %u bytes\n", devProp.memPitch);
    printf("Maximum threads per block:                     %d\n", devProp.maxThreadsPerBlock);
    printf("Maximum of block dimension x:                  %d\n", devProp.maxThreadsDim[0]);
    printf("Maximum of block dimension y:                  %d\n", devProp.maxThreadsDim[1]);
    printf("Maximum of block dimension z:                  %d\n", devProp.maxThreadsDim[2]);
    printf("Maximum of grid dimension  x:                  %d\n", devProp.maxGridSize[0]);
    printf("Maximum of grid dimension  y:                  %d\n", devProp.maxGridSize[1]);
    printf("Maximum of grid dimension  z:                  %d\n", devProp.maxGridSize[2]);
    printf("Peak Memory Bandwidth (GB/s):                  %.1f\n", 2.0*devProp.memoryClockRate*(devProp.memoryBusWidth/8)/1.0e6);
    printf("Texture alignment:                             %u\n", devProp.textureAlignment);
    printf("Concurrent copy and execution:                 %s\n", (devProp.deviceOverlap ? "Yes" : "No"));
    printf("Maximum threads per multiprocessor             %d\n", devProp.maxThreadsPerMultiProcessor);
    printf("Kernel execution timeout:                      %s\n", (devProp.kernelExecTimeoutEnabled ? "Yes" : "No"));
    printf("Theoretical Performance:\n");
    printf(" - FP32 (float) performance:                   %.1f TFLOPS\n", 2*getSPcores(devProp)*(devProp.clockRate/1000000.0)/1000.0);
    return;
}
 
void device_info() {
    // Number of CUDA devices
    int devCount;
    cudaGetDeviceCount(&devCount);
    printf("CUDA Device Query...\n");
    printf("There are %d CUDA devices.\n", devCount);
 
    // Iterate through devices
    for (int i = 0; i < devCount; ++i) {
        // Get device properties
        printf("\nCUDA Device #%d\n", i);
        cudaDeviceProp devProp;
        cudaGetDeviceProperties(&devProp, i);
        printDevProp(devProp);
    }
}
