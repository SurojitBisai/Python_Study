
def compute_hcf(x, y):  # Corrected function definition
    if x > y:
        smaller = y  # Fix logic: smaller value is the minimum of x and y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf  # Moved return outside the loop
num1 = 54
num2 = 24
print("The HCF of two numbers is:", compute_hcf(num1, num2))
