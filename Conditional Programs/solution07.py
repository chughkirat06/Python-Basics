# Coffee customization

"""
Customize a coffee order:
"Small", "Medium", or "Large"
with an option of "Extra Shot" of espresso.
"""

def get_coffee_size():
    """
    Prompts the user to select a coffee size and returns the selected size.
    """

    while True:
        size = input("Select coffee size (small, medium, or large): ").strip().lower()

        if size == "small":
            return "Small"
        elif size == "medium":
            return "Medium"
        elif size == "large":
            return "Large"
        else:
            print("No such coffee size is available. Please enter 'small', 'medium', or 'large'.")

def ask_for_extra_shot():
    """
    Prompts the user to decide whether to add an extra shot of espresso.
    """

    while True:
        extra_shot = input("Add extra shot of espresso (yes, no): ").strip().lower()

        if extra_shot in ["yes", "no"]:
            return extra_shot == 'yes'
        else:
            print("Please answer with 'yes' or 'no'.")

def main():
    # Get the coffee size
    size = get_coffee_size()

    # Ask for extra shot
    extra_shot = ask_for_extra_shot()

    # Print the final coffee order
    if extra_shot:
        print(f"{size} coffee with an extra shot of espresso.")
    else:
        print(f"{size} coffee")

if __name__ == "__main__":
    main()