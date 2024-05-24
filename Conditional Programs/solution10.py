# Pet food recommendation

"""
Recommend a type of pet food based on the pet's species and age.
(e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)
"""

def get_pet_species():
    """
    Prompts the user to enter the pet species and validates the input.

    Returns:
    str: The pet species (either "dog" or "cat").
    """

    while True:
        pet_species = input("Enter pet species (dog or cat): ").strip().lower()
        if pet_species in ["dog", "cat"]:
            return pet_species
        else:
            print("Invalid pet species. Please enter 'dog' or 'cat'.")

def get_pet_age():
    """
    Prompts the user to enter the pet age and validates the input.

    Returns:
    int: The pet age in years.
    """

    while True:
        try:
            pet_age = int(input("Enter dog age (in years): "))
            if pet_age >= 0:
                return pet_age
            else:
                print("Please enter a non-negative age.")
        except ValueError:
            print("Please enter a valid integer for the age.")

def recommend_food(pet_species, pet_age):
    """
    Recommends a type of pet food based on the pet's species and age.

    Parameters:
    pet_species (str): The species of the pet (either "dog" or "cat").
    pet_age (int): The age of the pet in years.
    """
    
    if pet_species == "dog":
        if pet_age < 2:
            print("Puppy food")
        else:
            print("Dog food")
    elif pet_species == "cat":
        if pet_age > 5:
            print("Senior cat food")
        else:
            print("Junior cat food")

def main():
    # Get pet species from user
    pet_species = get_pet_species()

    # Get pet age from user
    pet_age = get_pet_age()

    # Recommend food based on species and age
    recommend_food(pet_species, pet_age)

if __name__ == "__main__":
    main()