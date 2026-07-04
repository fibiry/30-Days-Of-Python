# 1. concatenate
word1 ='Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = 'Python'
print(word1 + ' ' + word2 + ' ' + word3 + ' ' + word4)

# 2. concatenate using format()
ex2 = 'Coding', 'For' , 'All' 
print('{} {} {}'.format(ex2[0], ex2[1], ex2[2]))

#3. declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding for All'

#4 print the variable company using print()
print(company)

#5. print the length of the company string using len() method and print()
print(len(company))

#6 change all the characters to uppercase letters using upper() method
print(company.upper())

#7 change all the characters to lowercase letters using lower() method
print(company.lower()) 

#8. use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9. cut(slice) out the first word of Coding For All string
print(company[0:6])

#10. check if Coding For All string contains a word Coding using the method index, find or other methods
print(company.index('Coding'))
print(company.find('Coding'))

#11. replace the word coding in the string 'Coding For All' to Python
print(company.replace('Coding', 'Python'))

#12. change Python for Everyone to Python for All using the replace method or other methods
company2 = 'Python for Everyone'
print(company2.replace('Everyone', 'All'))

#13. split the string 'Coding For All' using space as the separator (split()) method
print(company.split(' '))

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

#15. What is the character at index 0 in the string Coding For All
print('the index 0 character in the string is:', company[0])

#16. What is the last index of the string Coding For All
print('the last index of the string is:', company[-1])

#17. What character is at index 10 in "Coding For All" string
print('the character at index 10 is:', company[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = 'Python For Everyone'
print('The acronym for "{}" is "{}"'.format(acronym, ''.join(word[0] for word in acronym.split())))

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
acronym2 = 'Coding For All'
print('The acronym for "{}" is "{}"'.format(acronym2, ''.join(word[0] for word in acronym2.split())))

#20. Use index to determine the position of the first occurrence of C in Coding For All
phrase = 'Coding For All'
print('The index of the first occurrence of "C" in "{}" is: {}'.format(phrase, phrase.index('C')))

#21. Use index to determine the position of the first occurrence of F in Coding For All
print('The index of the first occurrence of "F" in "{}" is: {}'.format(phrase, phrase.index('F')))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People
phrase2 = 'Coding For All People'
print('The index of the last occurrence of "l" in "{}" is: {}'.format(phrase2, phrase2.rfind('l')))

#23. Use index or find to find the position of the first occurrence of the word "because" in the following sentence:
sentence = 'You cannot end a sentence with because because because is a conjunction'
print('The index of the first occurrence of "because" in "{}" is: {}'.format(sentence, sentence.index('because')))

#24. Use rindex to find the position of the last occurrence of the word "because" in the previous sentence:
print('The index of the last occurrence of "because" in "{}" is: {}'.format(sentence, sentence.rindex('because')))

#25. Slice out the phrase "because because because" in the sentence:
print('The sliced phrase is:', sentence[sentence.index('because'):sentence.rindex('because') + len('because')])

#26. Find the position of the first occurrence of the word "because" in the sentence using find() method:
print('The index of the first occurrence of "because" in "{}" is: {}'.format(sentence, sentence.find('because')))

#27. Slice out the phrase "because because because" in the sentence:
start_index = sentence.find('because')
end_index = sentence.rindex('because') + len('because')
print('The sliced phrase is:', sentence[start_index:end_index])

#28. Does ''Coding For All'' start with a substring Coding?
print('Does "{}" start with "Coding"? {}'.format(company, company.startswith('Coding')))

#29. Does ''Coding For All'' end with a substring coding?
print('Does "{}" end with "coding"? {}'.format(company, company.endswith('coding')))

#30. "   Coding For All      "  , remove the left and right trailing spaces in the given string.
string_with_spaces = "   Coding For All      "
print('The string with trailing spaces removed is: "{}"'.format(string_with_spaces.strip()))

#31. Which one of the following variables return True when we use the method isidentifier():
variable1 = '30DaysOfPython'
variable2 = 'thirty_days_of_python'
if variable1.isidentifier():
    print(variable1, 'is a valid identifier.')
else:
    print(variable2, 'is a valid identifier.')

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('The joined string is: {}'.format(' # '.join(python_libraries)))

#33. Use the new line escape sequence to separate the following sentences.
sentence1 = 'I am enjoying this challenge.'
sentence2 = 'I just wonder what I will be doing in the future.'
print('{}\n{}'.format(sentence1, sentence2))

#34. Use a tab escape sequence to write the following lines.
print('Name\t\tAge\tCountry\tCity\nSanty\t33\tColombia\tMedellin')

#35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
text = 'The area of a circle with radius {} is {} meters square.'.format(radius, area)
print(text)

#36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6
print('8 + 6 = {}'.format(a + b))
print('8 - 6 = {}'.format(a - b))
print('8 * 6 = {}'.format(a * b))
print('8 / 6 = {:.2f}'.format(a / b))
print('8 % 6 = {}'.format(a % b))
print('8 // 6 = {}'.format(a // b))
print('8 ** 6 = {}'.format(a ** b))
