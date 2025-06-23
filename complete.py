#void
def convert_and_print_to_fahrenheit(celsius_temp):
    fahrenheit=(celsius_temp * 9/5)+32
    print(f"{celsius_temp:.2f}°C is equal to {fahrenheit:.2f}°F")

#function
def convert_to_celsius(fahrenheit_temp):
    celsius=(fahrenheit_temp - 32)*5/9
    return celsius

#main
def main():
    while True:
        try:
            temp_input=float(input("Enter the temperature value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the temperature.")

    while True:
        scale = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if scale == 'C':
            convert_and_print_to_fahrenheit(temp_input)
            break
        elif scale == 'F':
            celsius = convert_to_celsius(temp_input)
            print(f"{temp_input:.2f}°F is equal to {celsius:.2f}°C")
            break
        else:
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

main()

            
