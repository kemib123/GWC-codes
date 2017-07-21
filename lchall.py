from random import *

#Create the list of words you want to choose from.

main_course = ( "chicken_nuggets" , "beef_wellington" , "burgers" , "pizza" , "steak")
sides = ("fries" , "salad" , "breadstick" ,"fruits" , "nuts")
desserts = ("cookies" , "icecream" ,"peach_cobler" , "cake" , "macaroon")

a = randint(0, len(main_course) -1)
b = randint(0, len(sides) -1)
c = randint(0, len(desserts) -1)

print(main_course [a], sides[b], desserts[c])
