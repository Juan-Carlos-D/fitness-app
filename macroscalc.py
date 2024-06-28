# macroscalc.py

def calculate_macros(weight, height, age, gender, activity_level):
    # Example calculation logic (you should adjust this based on your specific formula)
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    calories = bmr * activity_factors[activity_level]
    protein = 1.5 * weight  # Example protein calculation
    carbohydrates = 3.5 * weight  # Example carbs calculation
    fats = 0.3 * calories / 9  # Example fats calculation

    return {
        'calories': round(calories),
        'protein': round(protein),
        'carbohydrates': round(carbohydrates),
        'fats': round(fats)
    }
