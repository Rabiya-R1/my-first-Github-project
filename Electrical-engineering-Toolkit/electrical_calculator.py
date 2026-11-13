import math

print("=" * 45)
print("      ELECTRICAL ENGINEERING TOOLKIT")
print("=" * 45)

print("\n1. Single Phase Power")
print("2. Energy Consumption")
print("3. Electricity Bill")
print("4. Three Phase Power")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    voltage = float(input("Voltage (V): "))
    current = float(input("Current (A): "))
    power = voltage * current
    print("Power =", power, "W")

elif choice == "2":
    power = float(input("Power (W): "))
    hours = float(input("Hours per day: "))
    days = int(input("Number of days: "))
    energy = power * hours * days / 1000
    print("Energy =", energy, "kWh")

elif choice == "3":
    units = float(input("Units consumed: "))
    rate = float(input("Rate per unit (Rs): "))
    bill = units * rate
    print("Estimated Bill = Rs.", bill)

elif choice == "4":
    voltage = float(input("Line voltage (V): "))
    current = float(input("Line current (A): "))
    pf = float(input("Power factor (0 to 1): "))

    apparent_power = math.sqrt(3) * voltage * current
    active_power = apparent_power * pf

    print("Apparent Power =", round(apparent_power, 2), "VA")
    print("Active Power =", round(active_power, 2), "W")

else:
    print("Invalid choice!")
