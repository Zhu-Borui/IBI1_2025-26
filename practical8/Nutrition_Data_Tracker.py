# 1. Define the class
class food_item:
    """A class to represent a food item and its nutritional values."""
    
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


# 2. Define the tracking function
def calculate_daily_nutrition(consumed_list):
    """
    Takes a list of food_item objects, calculates totals,
    prints a report, and issues warnings if limits are exceeded.
    """
    
    # Initialize running totals
    total_calories = 0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    
    # Loop through the list and sum the attributes
    for item in consumed_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbohydrates
        total_fat += item.fat
        
    # Report the totals
    print("--- 24-Hour Nutritional Summary ---")
    print(f"Total Calories:      {total_calories}")
    print(f"Total Protein:       {total_protein:.1f} g")
    print(f"Total Carbohydrates: {total_carbs:.1f} g")
    print(f"Total Fat:           {total_fat:.1f} g")
    
    # Check for warnings (Calories > 2500 OR Fat > 90g)
    if total_calories > 2500 or total_fat > 90:
        print("\n*** NUTRITIONAL WARNING ***")
        if total_calories > 2500:
            print(f"- High Calorie Intake: You have consumed {total_calories} calories (Limit: 2500).")
        if total_fat > 90:
            print(f"- High Fat Intake: You have consumed {total_fat:.1f} g of fat (Limit: 90 g).")
    print("-" * 35 + "\n")


# Example
if __name__ == "__main__":
    
    # Create several food_item instances
    # Using the example from the prompt:
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    
    # Creating some other items
    chicken_breast = food_item("Chicken Breast", 284, 53.4, 0, 6.2)
    rice = food_item("Cup of White Rice", 205, 4.3, 44.5, 0.4)
    double_cheeseburger = food_item("Double Cheeseburger", 850, 48, 42, 54)
    large_fries = food_item("Large Fries", 510, 6, 67, 24)
    milkshake = food_item("Chocolate Milkshake", 800, 15, 120, 25)

    
    # A moderate day
    print("SCENARIO 1: Moderate Diet")
    diet_day_1 = [apple, apple, chicken_breast, rice]
    calculate_daily_nutrition(diet_day_1)
    
    
    # A day that triggers the warnings 
    print("SCENARIO 2: High Calorie/High Fat Diet")
    diet_day_2 = [double_cheeseburger, double_cheeseburger, large_fries, milkshake]
    calculate_daily_nutrition(diet_day_2)