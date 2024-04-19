# Importuje bibliotekę NumPy
import numpy as np 

# Pyta o liczbę elementów wektorze
n = int(input("Enter number of elements : "))

# Wiersz poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map() dla wektora
list1 = list(map(int, 
	input("\nEnter the numbers : ").strip().split()))[:n]


# Tworzy wektor 1 
# Wektor jako szereg 
vector1 = np.array(list1) 

# Wartość skalara  
scalar = int(input("Enter the value of scalar : "))

# Pokazuje poziomy wektor 
print("Horizontal Vector : " + str(vector1)) 
  
# Drukuje wartość skalara 
print("Scalar : " + str(scalar)) 
   
# Mnoży wektor przez skalar 
# s * v = (s * v1, s * v2, s * v3) 
scalar_mul = vector1 * scalar 
  
# Drukuje wynik 
print("Scalar Multiplication : " + str(scalar_mul)) 