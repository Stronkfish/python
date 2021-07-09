# Choose Conversion MPH or KPH 
main = input("Stonkfish Brand MPH/KPH Converter\n\nMPH = Convert KPH to MPH\nKPH = Convert MPH TO KPH\n\n")
conv = ""

# KPH to MPH Conversion
if main.upper() == "MPH":
    conv = int(input("\nEnter the speed in KPH to convert it into MPH: "))
    print(f"\nKPH: {conv}\nMPH: {conv*0.6214}\n")

# MPH to KPH Conversion
if main.upper() == "KPH": 
    conv = int(input("\nEnter the speed in MPH to convert it into KPH: "))
    print(f"\nMPH: {conv}\nKPH: {conv*1.6093}\n")
