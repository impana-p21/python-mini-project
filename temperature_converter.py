print("Temperature Converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose option: ")

if choice == "1":
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", round(f, 2))

elif choice == "2":
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Celsius:", round(c, 2))

else:
    print("Invalid option.")
