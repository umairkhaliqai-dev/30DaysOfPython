# Pyhton strings are the sequences of characters and we can un pack the string to extract any one character by nominationg it to corresponding variable.
#Unpacking
country = 'United Kingdom'
a,b,c,d,e,f,g,h,i,j,k,l,m,n = country
print(f)
print(k)
print(n)

#accessing with index
city = 'Newcastle'
letter = city[0]
print(letter)
last_index = len(city) -1
last = city[last_index]
print(last)
reverse = city[-1]
print(reverse)
second_reverse = city[-9]
print(second_reverse)
#so in reverse stage there is no need to put formula of len(city) -1 but we can inject the exact figure where it is positioned with a minus sign e.g. -1,-2...

language = 'Python'
first_three = language[0:3] # this is slicing a string into sub string.
print(first_three)

last_three = language[:5]
print(last_three)

print()
# reversing string
Greet = "Hello world!"
print(Greet[::-1])

language = 'Pythonzr'
pto = language[0:7:3] # skipping character.
print(pto) # Pto
