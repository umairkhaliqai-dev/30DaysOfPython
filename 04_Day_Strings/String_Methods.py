challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

print()
challenge = 'THIRTY DAYS OF PYTHON' # as text is capital si python is cas-sensitive.
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`
print()
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

print()
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

print()
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs(10))   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

print()
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print()
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
print()
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

print()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 7)) # error if num either than 7

print()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 7)) # error if nim eitherr than 7
print(challenge.rindex('on', 8)) # 19 # 8 is to ask to look for substring from 8th onwards.

print()
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

print()
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

print()
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

print()
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdigit())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True it is not whole number decimal from 0-9 but a numeric exponent as power 2 so still it counts as digit.
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

print()
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

print()
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

print()
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
print()
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
print()
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

print()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

print()
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py' # so strip() follows as tunnel cutting where as .replace() acts as vaccum.
print()
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

print()
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

print()
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

print()
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

print()
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False


print()
print("User input startwith")
print("=" *33)
command = input("How can I help you? ").lower()

if command.startswith("run"):
    print("Starting the program...")
elif command.startswith("help"):
    print("Opening the manual...")
else:
    print("Command not recognized.")

    print()
url = "https://github.com/asabeneh"

if url.startswith("https"):
    print("The connection is secure.")
else:
    print("Warning: This site might not be secure!")
