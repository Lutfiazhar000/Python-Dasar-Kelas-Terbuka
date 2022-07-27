import numpy as np

list_a = [2,3,4,5]
vector_a = np.array([2,3,4,5])


print(list_a)
print(vector_a)
print(f"list_a = {list_a}")
print(f"vector_a = {vector_a}") # sama seperti list tp lebih rapi 

# operasi
# print(list_a**2) # akan error
print(vector_a**2) 
print(vector_a*6)

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix_b = \n{matrix_b}")
print(f"matrix_b^3 = \n{matrix_b**3}")

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones d = \n{ones_d}")

hitung_matrix = matrix_b + matrix_b**2 + ones_d
print(f"hitung_matrix = \n{hitung_matrix}")