# This block of code changes the year on a list of dates.
# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = []

# The for loop checks each "year" element in the list "years".
for year in years:

    # The if-statement checks if the "year" element ends with the
    # substring "2023".
    if year.endswith("2023"):
        new = year.replace("2023", "2024")

        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)
    # If False, the original "year" element will be appended to the "updated_years" list unchanged.
    else:
        updated_years.append(year)

print(updated_years)
#------------------------------------------------------------------

# This list comprehension creates a list of squared numbers (n*n). It
# accepts two integer variables through the function’s parameters.
def squares(start, end):
    # The list comprehension calculates the square of a variable integer
    # "n", where "n" ranges from the "start" to "end" variables inclusively.
    # To be inclusive in a range(), add +1 to the end of range variable.
    return [n * n for n in range(start, end + 1)]

print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#--------------------------------------------------------------------

# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the
# element and adds a dash between the element and the moved character.
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):

# Initialize "new_string" as a string data type by using empty quotes.
    new_string = ""
    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:

        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items:
        # + Each list "element" (starting at index position [1:]),
        # + a dash "-",
        # + append the first character of the "element" (using the index
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-"  + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string

print(change_string("1one 2two 3three 4four 5five"))

#-----------------------------------------------------------------------
# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1,
# element2, element3".
def list_elements(list_name, elements):

    # This task can be completed in a single line of code. The
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"