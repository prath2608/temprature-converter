
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def temperature_converter():
    print("Temperature Unit Converter")
    print("1. Celsius\n2. Fahrenheit\n3. Kelvin")
    
    # Get user input for temperature and unit
    temperature = float(input("Enter the temperature value: "))
    original_unit = int(input("Enter the original unit (1 for Celsius, 2 for Fahrenheit, 3 for Kelvin): "))
    
    if original_unit == 1:
        # Convert from Celsius
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif original_unit == 2:
        # Convert from Fahrenheit
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif original_unit == 3:
        # Convert from Kelvin
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid input. Please enter a valid unit (1, 2, or 3).")

# Run the temperature converter
temperature_converter()
