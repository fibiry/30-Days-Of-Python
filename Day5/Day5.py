fruits = ["banana", "orange", "mango", "lemon"]
orange_and_mango = fruits[0:2:3]  # it does not include the first index
print(orange_and_mango)

a = "lemon" in fruits
print(a)

fruits.append("uvas")
fruits.append("kiwi")
fruits.append("granadilla")
# it will add the elements at the end of the list

print(fruits)


fruits.insert(3, "piña")
delete = fruits[2]
fruits.remove(delete)

print(fruits)
fruits.pop(6)
print(fruits)

# print(fruits.index("orange"))

# Excercices day 5

# 1. Declare an empty list

empty_list = []

# 2. Declare a list with more than 5 items

streamers = ["Rubius", "Auronplay", "Axozer", "Ibai", "Tanizen", "xXThe FocusXx"]

# 3. Find the length of your list
how_long = len(streamers)
print(how_long)

# 4. Get the first item, the middle item and the last item of the list
first_streamer = streamers[0]
middle_streamer = streamers[2]
last_streamer = streamers[-1]
print(first_streamer, middle_streamer, last_streamer)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = [
    "Santy",
    33,
    1.80,
    "soltero",
    "Calle 12A # 1580 - 2500",
]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()

print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# 10. Print the list after modifying one of the companies
it_companies[1] = "bing"  # Replace 'Google' with 'bing'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Nvidia")

# 12. Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "AMD")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()  # Change 'Facebook' to uppercase
print(it_companies)

# 14. Join the it_companies with a string '#;  '
it_companies_string = "#; ".join(it_companies)
print(it_companies_string)

# 15. Check if a certain company exists in the it_companies list.
company_to_check = "AMD"
exists = company_to_check in it_companies
print(exists)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)

# 19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)

# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
middle_companies = it_companies[middle_index : middle_index + 1]
print(middle_companies)

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
it_companies.pop(middle_index) + 1

# 23. Remove the last IT company from the list
it_companies.pop(-1)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
full_stack = front_end + back_end
print(full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack_copy. Then insert Python and SQL after Redux.
full_stack_copy = full_stack.copy()
full_stack_copy.insert(full_stack_copy.index("Redux") + 1, "Python")
full_stack_copy.insert(full_stack_copy.index("Python") + 1, "SQL")
print(full_stack_copy)

# Exercises: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sort the list and find the min and max age
ages.sort(reverse=True)
min_age = ages[-1]
max_age = ages[0]
print("the min age is: ", min_age, "and the max age is: ", max_age)
# add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)
# find the median age (one middle item or two middle items divided by two)
median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
print("the median age is: ", median_age)
# find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print("the average age is: ", average_age)
# find the range of the ages (max minus min)
# organized_age = ages.sort()
# max_age = ages[0]
# min_age = ages[-1]
range_of_ages = max_age - min_age
print(range_of_ages)
# Compare the value of (min - average) and (max - average), use abs() method

min_minus_av = abs(min_age - average_age)
max_minus_av = abs(max_age - average_age)

print(min_minus_av, max_minus_av)


# 1. Find the middle country(ies) in the countries list
countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]
middle_countries = (
    len(countries) // 2,
    len(countries) // 2 + 1,
)
print(middle_countries)
# print(middle_countries[0], ", ", middle_countries[1])
# print(countries.index[middle_countries[0]], countries.index[middle_countries[1]])

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
half_countries = len(countries) // 2
total_countries = len(countries)
print(total_countries)
is_even = len(countries) % 2 == 0
print(is_even)
if is_even:
    pair_list1 = countries[0:half_countries]
    pair_list2 = countries[half_countries:]
    print(pair_list1, " ", pair_list2)
else:
    odd_list1 = countries[0 : half_countries + 1]
    odd_list2 = countries[half_countries + 1 :]
    print(odd_list1, " ", odd_list2)

print(
    'La primera "mitad" tiene ',
    len(odd_list1),
    " paises y la segunda tiene ",
    len(odd_list2),
    " paises.",
)
