def calculate_macros(weight, height, age, gender, activity_level, goal, weight_unit='kg', height_unit='cm'):
    # Convert weight to kg if in pounds
    if weight_unit == 'lbs':
        weight = weight * 0.453592

    # Convert height to cm if in inches
    if height_unit == 'inches':
        height = height * 2.54

    # Calculate BMR
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Activity factors
    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    maintenance_calories = bmr * activity_factors[activity_level]

    # Adjust calories based on goal
    if goal == 'maintain':
        calories = maintenance_calories
    elif goal == 'gain_slow':
        calories = maintenance_calories + 250  # Gain ~0.5 lb per week
    elif goal == 'gain_fast':
        calories = maintenance_calories + 500  # Gain ~1 lb per week
    elif goal == 'lose_slow':
        calories = maintenance_calories - 250  # Lose ~0.5 lb per week
    elif goal == 'lose_fast':
        calories = maintenance_calories - 500  # Lose ~1 lb per week

    # Adjust macronutrients based on goal
    if goal in ['maintain', 'gain_slow', 'gain_fast']:
        protein = 2.0 * weight  # grams per kg of body weight
        fats = 0.3 * calories / 9  # grams of fat
        carbohydrates = (calories - (protein * 4 + fats * 9)) / 4  # grams of carbohydrates
    else:  # For weight loss
        protein = 2.2 * weight  # grams per kg of body weight
        fats = 0.25 * calories / 9  # grams of fat
        carbohydrates = (calories - (protein * 4 + fats * 9)) / 4  # grams of carbohydrates

    return {
        'calories': round(calories),
        'protein': round(protein),
        'carbohydrates': round(carbohydrates),
        'fats': round(fats)
    }
