p=float(input("Enter the principle amount:"))
r=float(input("Enter the rate of interest:"))
n=float(input("Enter the time period in Years:"))

print(f"The Compound interest for the princile value= {p}, rate of interest= {r}, Time period= {n} is \n\nCompound Interest =",p*(1+r/100)**n-p)