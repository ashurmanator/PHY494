#temperature conversion

temperatures = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0]
temp_kelvin = []
for theta in temperatures:
    T = (theta - 32) * (5/9) +273.15
    print(T)
    temp_kelvin.append(T)

print("Conversion complete")
print(temp_kelvin)
