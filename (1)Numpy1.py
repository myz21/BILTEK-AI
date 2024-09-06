import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

#veri tipini yazdırıyoruz
print(type(py_list))
print(type(np_array))

py_multiDim = [[1,2,3],[4,5,6],[7,8,9]]

#tek boyutlu array 3x3 matrix olarak yazdırılıyor.
np_multiDim = np_array.reshape(3,3)

print(np_multiDim)
print(py_multiDim)

#dizilerimizin boyut sayısını yazdırıyoruz.
print(np_multiDim.ndim)
print(np_array.ndim)

#dizilerin her eksenindeki uzunluğu yazdırıyoruz.
print(np_array.shape)
print(np_multiDim.shape)
