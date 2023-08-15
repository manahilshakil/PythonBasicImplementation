fruits = ["melon","mango","pines"]
fruits.append("banana")
fruits.insert(3,"orange")
print(fruits)
fruits[3] = "new"
#removing
fruits.remove("melon")
fruits.pop(2)

#tuples
result=(60,1,1)
sec,min,hr = result
print(sec,min,hr)

#working
students=["emilyy","rachel","blair","serena"]
char = 0
for student in students:
    char += len(students)

print("total characters = {}".format(char))

for index,student in enumerate(students):
    print("{} - {}".format(index+1,student))

def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)
    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

people = [("manahil@gmail.com", "manahil shakil"), ("eishal@gmail.com", "eishal shakil")]

def email_creator(people):
    r = []
    for email, name in people:
        r.append("{} <{}>".format(name, email))  # Corrected the placement of the formatting placeholder
    return r

print(email_creator(people))

#list comprehension
#The odd_numbers function returns a list of odd numbers between 1 and n
def odd_numbers(n):
	return [x for x in range(1,n+1) if x%2==1]

print(odd_numbers(5))
print(odd_numbers(10))
print(odd_numbers(11))
print(odd_numbers(1))
print(odd_numbers(-1))