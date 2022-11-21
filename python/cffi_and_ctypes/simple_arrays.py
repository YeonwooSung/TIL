import ctypes

IntArray5 = ctypes.c_int * 5
cint_array = IntArray5(1, 2, 3, 4, 5)

FloatArray2 = ctypes.c_float * 2
cfloat_array = FloatArray2(0, 3.14)

print(cint_array[0])
print(cint_array[1])
print(cint_array[2])
print(cint_array[3])
print(cint_array[4])

print(cfloat_array[0])
print(cfloat_array[1])
