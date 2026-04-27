# 1 Declare function having sum of 2 parameters: 
def add_two_numbers(a,b):
    return a + b
print(add_two_numbers(45, 95))  
 # Are of circle
import math
def area_of_circle(r):
    return math.pi * r ** 2

print(area_of_circle(5))  
# arbitrary number argument
def add_all_nums(*nums):
    if not all(isinstance(n, (int, float)) for n in nums):
        return "All items must be numbers"
    return sum(nums)

print(add_all_nums(1, 2, 0.98, 4)) 
# temperature conversion 
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(convert_celsius_to_fahrenheit(0))   
print(convert_celsius_to_fahrenheit(100))  
# months for season 
def check_season(month):
    if month in ['September','October','November']:
        return 'Autumn'
    elif month in ['December','January','February']:
        return 'Winter'
    elif month in ['March','April','May']:
        return 'Spring'
    else:
        return 'Summer'
result = check_season('October')
print(result)
