/* ---------------------------------------------
Makefile constructed configuration:
----------------------------------------------*/
#if !defined(KOKKOS_MACROS_HPP) || defined(KOKKOS_CORE_CONFIG_H)
#error "Do not include KokkosCore_config.h directly; include Kokkos_Macros.hpp instead."
#else
#define KOKKOS_CORE_CONFIG_H
#endif

#define KOKKOS_VERSION 30500

/* Execution Spaces */
#define KOKKOS_ENABLE_CUDA
#define KOKKOS_COMPILER_CUDA_VERSION 115
#define KOKKOS_ENABLE_SERIAL
#ifndef __CUDA_ARCH__
#define KOKKOS_USE_ISA_X86_64
#endif
/* General Settings */
#define KOKKOS_ENABLE_DEPRECATED_CODE_3
#define KOKKOS_ENABLE_CXX17
#define KOKKOS_ENABLE_COMPLEX_ALIGN
#define KOKKOS_ENABLE_LIBDL
#define KOKKOS_ENABLE_HWLOC
/* Optimization Settings */
/* Cuda Settings */
#define KOKKOS_ARCH_AMD_ZEN2
#define KOKKOS_ARCH_AMD_AVX2
#define KOKKOS_ARCH_AMPERE
#define KOKKOS_ARCH_AMPERE80
