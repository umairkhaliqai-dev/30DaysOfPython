# List of 10 students with their ages.
age_lst = [19, 22, 19, 24, 20, 25, 26, 24, 25, 25]
age_lst.sort()
min_age = min(age_lst)
max_age = max(age_lst)
print()
print(age_lst)
print(f"min age is {min_age} and max age is {max_age}")
print("Thank You !")
print()
age_lst.append(min_age)
age_lst.append(max_age)
print(age_lst)

age_lst.sort()
print(f"sorted age list after adding: {age_lst}")
n = len(age_lst)
print(n)
if n % 2 == 0:
    middle_index1 = n // 2 -1
    middle_index2 = n // 2
    median = (age_lst[middle_index1] + age_lst[middle_index2]) / 2
    print(f"even numbers of item: {n}")
    print(f"first middle index: {middle_index1} & second middle inex: {middle_index2}")
    print(f"index 1 value: {age_lst[middle_index1]} & index 2 value: {age_lst[middle_index2]}")
    
else: 
    middle_index = n // 2
    median = age_lst[middle_index]
    print(f"odd numbers of item: {n}")
    print(f"middle index@: {middle_index}")
    print(f"middle value: {age_lst[middle_index]}")

print(f"\n Median AGE is {median}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe']
n = len(countries)
middle_index = n // 2
middle_country = (countries[middle_index])
print(f"\n number of countries in list: {n}")
print(f"the middle index of list is {middle_index}")
print(f"the middle country is {middle_country} \n")
print()
print("=" *100)
print()
n = len(countries)
if n % 2 == 0:
    Middle_index = n // 2              # 4 spaces 
    first_half = countries[:Middle_index]   
    second_half = countries[Middle_index]
else:
    mid = (len(countries) + 1) // 2
    first_half = countries[:mid]
    second_half = countries[mid:]

print(f"first half list: {first_half}")
print(f"second half list is {second_half}")

print()
print("the short other way is as below:") #short way !
print("£" * 50)
n = len(countries)
mid = (n + 1) // 2  # This math handles both even and odd correctly

first_half = countries[:mid]
second_half = countries[mid:]

print(f"First half length: {len(first_half)}")
print(f"Second half length: {len(second_half)}")
print(first_half)
print(second_half)
print()
print()
print("Unpacking countries")
tech_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Unpacking: first three go to variables, the rest go into a list called 'scandic'
c1, c2, c3, *scandic = tech_countries

print(c1, c2, c3)    # China Russia USA
print(scandic)       # ['Finland', 'Sweden', 'Norway', 'Denmark']


