#These are solutions to 6.8.3-6.8.4
#Creating a list with ingredients for köttfärsssås

ingredients = ['köttfärs', 'grädde', 'fond', 'lök', 'svamp', 'kryddor']

#Printing the third ingredient

print(ingredients[2].capitalize())

#Create a list with 3 numbers

my_numbers = [2, 3, 5]

#Multiply the numbers in the list by using their indexes and
#print their product

product = my_numbers[0] * my_numbers[1] * my_numbers[2]

print(product)

#Create a list of names and print them with spaces inbetween 
#on the same line

my_names = ['Daz', 'Dazpoet', 'daZ_poet']

print (my_names[0] + " " + my_names[1] + " " + my_names[2])

#Create a dictionary with a few favorite movies and their corresponding
#main antagonist

my_dict = {'GoldenEye':'James Bond','Iron Man':'Tony Stark', 'Star Trek':'Spock'}

#Print an example or two of the antagonists based on the movies

print(my_dict['GoldenEye'])
print(my_dict['Star Trek'])

#Print all of them using a for-loop
for i in my_dict:
    print(i)
    print(my_dict[i])