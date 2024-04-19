# importing numpy 
import numpy as np 

# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
list1 = list(map(int, 
	input("\nEnter the numbers : ").strip().split()))[:n]


# creating a vector1 
# vector as row 
vector1 = np.array(list1) 

# scalar value  
scalar = int(input("Enter the value of scalar : "))

# showing horizontal vector 
print("Horizontal Vector : " + str(vector1)) 
  
# printing scalar value 
print("Scalar : " + str(scalar)) 
   
# getting scalar multiplication value 
# s * v = (s * v1, s * v2, s * v3) 
scalar_mul = vector1 * scalar 
  
# printing dot product 
print("Scalar Multiplication : " + str(scalar_mul)) 