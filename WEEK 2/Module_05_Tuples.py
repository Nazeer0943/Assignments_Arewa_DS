# Question 1, Create an empty tuple
empty_tuple = tuple()
# Question 2, Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_sisters = ("Sara", "Hauwa", "Amina", "Aisha")
my_brothers = ("Abubakar", "Usman", "Sani", "Iliyas")
# Question 3, Join brothers and sisters tuples and assign it to siblings
siblings = my_sisters + my_brothers
print(siblings)
# Question 4, How many siblings do you have?
print(len(siblings))
# Question 5, Modify the siblings tuple and add the name of your father and mother and assign it to family_members
new_list = ("father", "mother")
family_members = siblings + new_list
print(family_members)

# Tuple Exercises: Level 2
#Unpack siblings and parents from family_members
siblings, parents, *rest = family_members
# 2, Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "orange")
vegetables = ("cabbage", "carrot", "shrump")
animal_product = ("cow_meat", "chicken", "beaf")
food_stuf_tp = fruits + vegetables + animal_product
print(food_stuf_tp)
food_stuf_tp = list(food_stuf_tp)
print(type(food_stuf_tp))
# Question 4, Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
import statistics

print(statistics.median(food_stuf_tp))
# 5, Slice out the first three items and the last three items from food_staff_lt list
print("the first three are:", food_stuf_tp[:3], "the last three:", food_stuf_tp[6:])
# Question 6, Delete the food_staff_tp tuple completely
del food_stuf_tp
# Question 7, Check if an item exists in tuple: Check if 'Estonia' is a nordic country,Check if 'Iceland' is a nordic country,nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

