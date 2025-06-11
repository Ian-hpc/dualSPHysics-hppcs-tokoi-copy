#!/bin/bash -x 
make -j 12 KOKKOS_USE_TPLS=hwloc KOKKOS_DEVICES=Cuda KOKKOS_ARCH=Zen2,Ampere80 KOKKOS_CXX_STANDARD=c++17 KOKKOS_PATH=~/kokkos/kokkos
