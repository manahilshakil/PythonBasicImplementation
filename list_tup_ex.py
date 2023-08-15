filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for files in filenames:
 if files.endswith(".hpp"):
  index = files.index(".")
  newfiles = files[:index] + ".h"
  newfilenames.append(newfiles)
 else:
  newfilenames.append(files)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
    say = ""
    texts = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        new_word = word[1:] + word[0] + "ay"
        texts.append(new_word)
    # Turn the list back into a phrase
    say = " ".join(texts)

    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


def group_list(group, users):
  members = ", ".join(users)
  return group +": " +members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


def guest_list(guests):
	for guest in guests:
		name,age,work = guest
		print("{} is {} years old and works as {}".format(name,age,work))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
