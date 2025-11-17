# Day 4 - If Conditions
# Contains: BMI calculator, city->country mapper, and same-country checker

def bmi_category(height_m: float, weight_kg: float) -> str:
    """Return BMI category given height (m) and weight (kg)."""
    if height_m <= 0:
        return "Invalid height"
    bmi = weight_kg / (height_m ** 2)
    # Use categories as per task
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

def task_bmi():
    print("\n=== BMI Calculator ===")
    try:
        height_input = input("Enter height in meters (e.g. 1.75): ").strip()
        weight_input = input("Enter weight in kilograms (e.g. 70): ").strip()
        height = float(height_input)
        weight = float(weight_input)
    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")
        return
    category = bmi_category(height, weight)
    print(f"Your BMI category is: {category}")

# City-country dataset (as given in task)
COUNTRY_CITIES = {
    "Australia": ["sydney", "melbourne", "brisbane", "perth"],
    "UAE": ["dubai", "abu dhabi", "sharjah", "ajman"],
    "India": ["mumbai", "bangalore", "chennai", "delhi"]
}

def find_country_by_city(city_name: str) -> str:
    """Return the country name if city is found, else return empty string."""
    city = city_name.strip().lower()
    for country, cities in COUNTRY_CITIES.items():
        if city in cities:
            return country
    return ""

def task_city_mapper():
    print("\n=== City -> Country Mapper ===")
    city = input("Enter a city name (e.g. Abu Dhabi): ").strip()
    if not city:
        print("No city entered.")
        return
    country = find_country_by_city(city)
    if country:
        print(f"{city} is in {country}")
    else:
        print(f"Sorry, {city} is not in our dataset.")

def task_same_country_checker():
    print("\n=== Same Country Checker ===")
    city1 = input("Enter the first city: ").strip()
    city2 = input("Enter the second city: ").strip()
    if not city1 or not city2:
        print("Please enter both cities.")
        return
    country1 = find_country_by_city(city1)
    country2 = find_country_by_city(city2)
    if country1 and country2:
        if country1 == country2:
            print(f"Both cities are in {country1}")
        else:
            print("They don't belong to the same country")
            print(f"{city1} -> {country1}, {city2} -> {country2}")
    else:
        missing = []
        if not country1:
            missing.append(city1)
        if not country2:
            missing.append(city2)
        print(f"Couldn't find these cities in dataset: {', '.join(missing)}")

def main():
    print("Day 4 - If Conditions\n")
    while True:
        print("\nChoose a task to run:")
        print("1 - BMI Calculator")
        print("2 - City -> Country Mapper")
        print("3 - Same Country Checker")
        print("0 - Exit")
        choice = input("Enter choice number: ").strip()
        if choice == "1":
            task_bmi()
        elif choice == "2":
            task_city_mapper()
        elif choice == "3":
            task_same_country_checker()
        elif choice == "0":
            print("Exiting Day 4 tasks. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3 or 0.")

if __name__ == "__main__":
    main()
