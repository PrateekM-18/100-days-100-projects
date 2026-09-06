def temperature_converter():
    print("\n----Temperatur Converter----")
    print("1. Celsius to Fahrenheit")
    print("2. Farenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter your choice: ")
    value = float(input("Enter the temperature: "))

    if choice == "1":
        result = (value * 9/5) + 32
        print(f"{value}°C - {result:.2f}°F")
    elif choice == "2":
        result = (value - 32) * 5/9
        print(f"{value}°F - {result:.2f}°C")
    elif choice == "3":
        result = value + 273.15
        print(f"{value}°C - {result:.2f}K")
    elif choice == "4":
        result = value - 273.15
        print(f"{value}K - {result:.2f}°C")
    else:
        print("Invalid choice!!!")


def length_converter():
    print("\n----Length Converter----")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Miles to Kilometer")
    print("4. Kilometer to Miles")
    print("5. Meter to Feet")
    print("6. Feet to Meter")

    choice = input("Enter your choice: ")
    value = float(input("Enter the length: "))

    if choice == "1":
        result = value / 1000
        print(f"{value}m - {result:.2f}km")
    elif choice == "2":
        result = value * 1000
        print(f"{value}km - {result:.2f}m")
    elif choice == "3":
        result = value * 1.609
        print(f"{value}mi - {result:.2f}km")
    elif choice == "4":
        result = value / 1.609
        print(f"{value}km - {result:.2f}mi")
    elif choice == "5":
        result = value * 3.281
        print(f"{value}m - {result:.2f}ft")
    elif choice == "6":
        result = value / 3.281
        print(f"{value}ft - {result:.2f}m")
    else:
        print("Invalid Choice!!!")   


def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Kilograms to Grams")
    print("4. Grams to Kilograms")

    choice = input("Choose an option: ")
    value = float(input("Enter the weight: "))

    if choice == "1":
        result = value * 2.20462
        print(f"{value} kg = {result:.2f} pounds")

    elif choice == "2":
        result = value * 0.453592
        print(f"{value} pounds = {result:.2f} kg")

    elif choice == "3":
        result = value * 1000
        print(f"{value} kg = {result:.2f} grams")
    elif choice == "4":
        result = value / 1000
        print(f"{value} grams = {result:.2f} kg")

    else:
        print("Invalid choice!")

def time_converter():
    print("\n--- Time Converter ---")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Hours to Minutes")
    print("4. Minutes to Hours")

    choice = input("Choose an option: ")
    value = float(input("Enter the time: "))

    if choice == "1":
        result = value / 60
        print(f"{value} seconds = {result:.2f} minutes")

    elif choice == "2":
        result = value * 60
        print(f"{value} minutes = {result:.2f} seconds")

    elif choice == "3":
        result = value * 60
        print(f"{value} hours = {result:.2f} minutes")

    elif choice == "4":
        result = value / 60
        print(f"{value} minutes = {result:.2f} hours")

    else:
        print("Invalid choice!")


#Main Program
def main():
    while True:
        print("\n====================")
        print("    UNIT CONVERTER    ")
        print("====================")
        print("1. Temperature")
        print("2. Length")
        print("3. Weight")
        print("4. Time")
        print("5. Exit")   

        choice = input("Enter the choice:")

        try:
            if choice == "1":
                temperature_converter()
            elif choice == "2":
                length_converter()
            elif choice == "3":
                weight_converter()
            elif choice == "4":
                time_converter()
            elif choice == "5":
                print("Exiting the process...")
                break
            else:
                print("Invalid choice!!!")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()