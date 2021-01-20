print("WELCOME TO TEMPERATURE CONVERTER")
print('===============================')
print('')
print('Celcius to Fahrenheit (1)')
print('Fahrenheit to Celcius (2)')
print('')
choice = int(input("Your choice (1) or (2)?"))

if choice == 1:
	temp = float(input('Enter temperature in Celcius: '))
	f = (temp*9/5) + 32
	print("Temperature in Fahrenheit = ", f)
else:
	temp = float(input('Enter temperature in Fahrenheit: '))
	c = (temp-32) * 5/9
	print("Temperature in Celcius = ", c)