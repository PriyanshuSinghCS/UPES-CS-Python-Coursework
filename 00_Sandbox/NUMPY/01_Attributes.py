import numpy as np

list1 = [10, 20, 30, 40, 50]
array1 = np.array(list1)
print(array1)
print("Dimension = ",array1.ndim)  # 1
print("Shape = ", array1.shape)
print("Size = ",array1.size)
print()


list2 = [[10,20,30], [40,50,60], [70,80,90]]
array2 = np.array(list2)
print(array2)
print("Dimension = ",array2.ndim)    # 2
print("Shape = ", array2.shape)
print("Size = ",array2.size)
print()


# For 3-D , shape = (depth,rows,column)
list3 = [[[10,20,30], [40,50,60]], [[70,80,90], [100, 120, 130]]]
array3 = np.array(list3)
print(array3)
print("Dimension = ",array3.ndim)   # 3
print("Shape = ", array3.shape)
print("Size = ",array3.size)
print()