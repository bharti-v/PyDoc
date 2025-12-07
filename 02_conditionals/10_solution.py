# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = "Cat"

age = 3 
if species == "Dog":
    if age < 2:
        food = "Puppy food"
    elif age <= 7:
        food = "Adult dog food"
    else:
        food = "Senior dog food"
elif species == "Cat":
    if age < 1:
        food = "Kitten food"
    elif age <= 5:
        food = "Adult cat food"
    else:
        food = "Senior cat food"    

else:
    food = "Unknown species"
print("Recommended food:", food)