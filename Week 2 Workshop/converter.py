print('Temperature Conversion program')

celsiusValue =  float(input('Enter celcius value to convert to fahrenheit'))
fahrenheightValue = celsiusValue * 9 / 5 + 32
kelvinValue = celsiusValue + 273.15

print('celsius value:', celsiusValue)
print('fahrenheit value:', fahrenheightValue)
print('kelvin value:', kelvinValue)