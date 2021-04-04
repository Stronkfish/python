# Choose whether to convert from Celsius to Fahrenheit and vice versa
main = input("Stronkfish Brand Temperature Converter\n\nCLS = Convert to Celsius\nFHR = Convert to Fahrenheit\n\n")

# Pre-Defined Variable
conv = ""

# If the User is Converting to Fahrenheit
if main.upper() == "FHR":
    conv = int(input("\nEnter the Temperature in Celsius to convert it into Fahrenheit: "))

# Fahrenheit = Celsius x 9/5 + 32
    print(f"\nCelsius: {conv} \nFahrenheit: {conv*9/5+32}")

# If the User is Converting to Celsius
if main.upper() == "CLS":
    conv = int(input("\nEnter the Temperature in Fahrenheit to convert it into Celsius: "))

# Celsius = (Fahrenheit - 32) x 5/9
    print(f"\nFahrenheit: {conv} \nCelsius: {(conv-32)*5/9}")
