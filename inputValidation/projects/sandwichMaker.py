import pyinputplus as pyip

# Prices dictionary
prices = {
    "bread": {
        "Wheat": 1.0,
        "White": 1.0,
        "Sourdough": 1.5
    },
    "protein": {
        "Chicken": 2.5,
        "Turkey": 3.0,
        "Ham": 3.0,
        "Tofu": 2.0
    },
    "cheeseType": {
        "Cheddar": 1.0,
        "Swiss": 1.5,
        "Mozzarella": 0.5
    },
    "condiments": {
        "mayo": 0.25,
        "mustard": 0.25,
        "lettuce": 0.3,
        "tomato": 0.3
    }
}

# User input prompts
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'])
protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'])
cheese = pyip.inputYesNo(prompt='Do you want Cheese?\n')

# Function for cheese selection
def chiss():
    if cheese == 'yes':
        cheeseType = pyip.inputChoice(['Cheddar', 'Swiss', 'Mozzarella'])
        return cheeseType
    else:
        return 'no'

cheeseType = chiss()

# User input for condiments
mayo = pyip.inputYesNo(prompt='Do you want mayo, mustard, lettuce or tomato?\n')

# Function for condiments selection
def mayoo():
    selected_condiments = []
    if mayo == 'yes':
        if pyip.inputYesNo(prompt='Do you want mayo?\n') == 'yes':
            selected_condiments.append("mayo")
        if pyip.inputYesNo(prompt='Do you want mustard?\n') == 'yes':
            selected_condiments.append("mustard")
        if pyip.inputYesNo(prompt='Do you want lettuce?\n') == 'yes':
            selected_condiments.append("lettuce")
        if pyip.inputYesNo(prompt='Do you want tomato?\n') == 'yes':
            selected_condiments.append("tomato")
    return selected_condiments

selected_condiments = mayoo()

# User input for number of sandwiches
sandwich_count = pyip.inputInt(prompt='How many sandwiches do you want?\n', min=1)

# Calculating the total cost
def calculate_total():
    total_price = prices["bread"][bread] + prices["protein"][protein]

    if cheeseType != 'no':
        total_price += prices["cheeseType"][cheeseType]

    # Add price for condiments if selected
    for condiment in selected_condiments:
        total_price += prices["condiments"][condiment]

    total_price *= sandwich_count  # Multiply by number of sandwiches
    return total_price

# Calculate the total price
total_price = calculate_total()

# Print out the summary and price
print(f"You ordered {sandwich_count} sandwich(es) with {bread} bread, {protein} protein, {cheeseType} cheese, "
      f"and {', '.join(selected_condiments) if selected_condiments else 'no condiments'}.")
print(f"Total price: ${total_price:.2f}")
