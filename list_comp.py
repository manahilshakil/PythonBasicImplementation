### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
print([x*2 for x in range(1,11)])
### Long form for loop
print("Long form code result:")
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)

#------------------------------------------------------------

### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)

#--------------------------------------------------------------

