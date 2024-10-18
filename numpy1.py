import numpy as np;

array = np.array(range(5));
print("one dimensional array")
print(array);
print("=============")
array_2d = np.array([range(4),[2,4,6,8]]);
print("two dimensional array")
print(array_2d.shape)
print(array_2d)
print("=============")

array_3d = array_2d.reshape(2,2,2)
print("three dimensional array")
print(array_3d.shape)
#How to interpret this three dimensional array?
#It is a one-dimensional array of two elements where each element is a two dimensional array
#each of the two dimensional array has two rows and two columns
print(array_3d)
print(array_3d[0][0][1])
print(array_3d[1][1][1])

#this notation also works
print(array_3d[1,1,1])

