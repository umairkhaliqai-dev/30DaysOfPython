
#NumPy (Numerical Python) is a powerful external library for scientific computing.
#  It introduces ndarray—a fast, memory-efficient N-dimensional array—and 
# provides vectorized operations, linear algebra, random number generation,
#  and advanced statistical functions.

import numpy as np

# Create a NumPy array (more efficient than list for math)
heights = np.array([170, 165, 180, 175, 160, 185])

# Vectorized operations
heights_in_meters = heights / 100

# Statistical methods directly on array
print(f"Mean: {np.mean(heights):.1f} cm")      # Mean: 172.5 cm
print(f"Median: {np.median(heights)} cm")      # Median: 172.5 cm
print(f"Std Dev: {np.std(heights):.1f} cm")    # Std Dev: 8.5 cm
print(f"Min: {np.min(heights)}, Max: {np.max(heights)}")  # Min: 160, Max: 185
print(heights_in_meters) # [1.7  1.65 1.8  1.75 1.6  1.85]

# Creating a float numpy array from list with a float data type parameter


    # Python list
python_list = [1,2,3,4,5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

#Creating a boolean a numpy array from list

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

# Creating multidimensional array using numpy
# A numpy array may have one or multiple rows and columns

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

### $$$ I have installed Anaconda and got a jupyter Notebook on it as well ££££
### This 