main = input("Stonkfish Brand MPH/KPH Converter\n\nMPH = Convert KPH to MPH\nKPH = Convert MPH TO KPH\n\nNOTE: Decimal Inputs Do Not Work\n\n") # Choose Conversion MPH or KPH (1)
k2m = "" # Pre-Define (2-3)
m2k = ""
if main.upper() == "MPH": # KPH to MPH Conversion (4-6)
    k2m = int(input("\nEnter the speed in KPH to convert it into MPH: "))
    print(f"\nKPH: {k2m}\nMPH: {k2m*0.6214}")
if main.upper() == "KPH": # MPH to KPH Conversion (7-9)
    m2k = int(input("\nEnter the speed in MPH to convert it into KPH: "))
    print(f"\nMPH: {m2k}\nKPH: {(m2k)*1.6093}")
