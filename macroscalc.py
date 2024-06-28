def calculate_macros(weight, height, age, gender, activity_level, goal, weight_unit, height_unit):
    if weight_unit == 'lbs':
        weight = weight * 0.453592  # Convert lbs to kg
    if height_unit == 'inches':
        height = height * 2.54  # Convert inches to cm

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

    maintenance_calories = bmr * activity_factors[activity_level]

    if goal == 'maintain':
        calories = maintenance_calories
        protein = 1.5 * weight
        carbohydrates = 3.5 * weight
        fats = 0.3 * calories / 9
    elif goal == 'gain_slow':
        calories = maintenance_calories + 250  # Gain ~0.5 lb per week
        protein = 1.8 * weight
        carbohydrates = 4.0 * weight
        fats = 0.35 * calories / 9
    elif goal == 'gain_fast':
        calories = maintenance_calories + 500  # Gain ~1 lb per week
        protein = 2.0 * weight
        carbohydrates = 4.5 * weight
        fats = 0.4 * calories / 9
    elif goal == 'lose_slow':
        calories = maintenance_calories - 250  # Lose ~0.5 lb per week
        protein = 1.8 * weight
        carbohydrates = 3.0 * weight
        fats = 0.25 * calories / 9
    elif goal == 'lose_fast':
        calories = maintenance_calories - 500  # Lose ~1 lb per week
        protein = 2.0 * weight
        carbohydrates = 2.5 * weight
        fats = 0.2 * calories / 9

    return {
        'calories': round(calories),
        'protein': round(protein),
        'carbohydrates': round(carbohydrates),
        'fats': round(fats)
    }
