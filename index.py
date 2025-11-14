def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    """Return BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def water_recommendation(weight):
    """Calculate daily water intake (in liters) based on weight"""
    return round(weight * 0.03, 2)

def display_summary(name, bmi, category, water):
    """Display member's health summary"""
    print("\n--- Member Health Summary ---")
    print(f"Name: {name}")
    print(f"BMI: {bmi}")
    print(f"BMI Category: {category}")
    print(f"Daily Water Recommendation: {water} liters")
    print("-----------------------------\n")

while True:
    action = input("Enter 'start' to process a new member or 'q' to quit: ").lower()

    if action == 'q':
        print("\nThank you for using the Fitness Center BMI & Hydration Tool!")
        break
    elif action == 'start':
        name = input("Enter member's name: ")
        try:
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in meters: "))
        except ValueError:
            print("Invalid input! Please enter numeric values for weight and height.\n")
            continue

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        water = water_recommendation(weight)

        display_summary(name, bmi, category, water)
    else:
        print("Invalid input! Type 'start' or 'q'.\n")

