first_name_one = "JoHn"
first_name_two = "   joHn   "
#Lower - Changes the string to every letter as low.
first_name_one = first_name_one.lower()
print(first_name_one)
#Strip - Removes spaces from the left and the right
# print(first_name_two)
first_name_two = first_name_two.strip()
# print(first_name_two)
#Both strip and lower
first_name_two = first_name_two.strip().lower()
# print(first_name_two)

# #Count - Used to count some characters in a string
# count_o = first_name_two.lower().count('oh')
# print(count_o)
# #Indexing - This is to access data in a string. Count from 0 or -1
# Slicing
# #First part represents the index (For index part start from 0) 
# #Second part represents the count (For count part start from 1)
print(first_name_one[1:3])

# #Type function - This is used type of variable. This is important to determine 
# #the operations that can be done.
print(type(first_name_one))

# #Split - Split the string according to a certain criteria

# mystring = "This is a list of items;item 1;item2;item 3"
# mysplit_string = mystring.split(";")
# print(mysplit_string)
# # What data type is mysplit_string? List (Array)

# #Concatenate - Joining or adding strings.
# my_first_name = "John"
# my_last_name = "Doe"
# my_full_name = my_first_name +" "+ my_last_name
# print(my_full_name)





