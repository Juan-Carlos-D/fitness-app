from flask import Flask, render_template, request
from faq import faq_data 
from macronutrients import macronutrients_data
from macroscalc import calculate_macros

app = Flask(__name__)

# Exercise Data
exercises = [
    {
        "Name": "Push-Ups",
        "Description": "Upper Body Pushing Movement",
        "Duration": 30,
        "Difficulty": "Medium",
        "Muscle Groups": ["Chest", "Triceps", "Shoulders"],
        "Instructions": [
            "1. Place your hands on the floor.",
            "2. Keep your body straight.",
            "3. Bend your elbows to lower your chest towards the ground.",
            "4. Then push back up."        
        ],
        "image_path": "Images/push-up.png"
    },
    
    {
        "Name": "Squats",
        "Description": "Lower Body Strengthening Movement",
        "Duration": 30,
        "Difficulty": "Medium",
        "Muscle Groups": ["Quadriceps", "Hamstrings", "Glutes"],
        "Instructions": [
            "1. Stand with your feet shoulder-width apart.",
            "2. Lower your body by bending your knees and hips.",
            "3. Keep your chest upright and your back straight.",
            "4. Return to the starting position by pushing through your heels."      
        ],
        "image_path": "Images/squat.png"        
    },
    
    {
        "Name": "Pull-Ups",
        "Description": "Upper Body Pulling Movement",
        "Duration": 30,
        "Difficulty": "Hard",
        "Muscle Groups": ["Lats", "Biceps", "Core"],
        "Instructions": [
            "1. Position yourself under a pull-up bar. Make sure it's at a reachable height.",
            "2. Hold the bar with both hands, palms facing away from you (overhand grip), and your hands shoulder-width apart.",
            "3. Begin hanging from the bar with your arms straight and feet off the ground. Your body should be in a straight line.",
            "4. Focus on engaging your core muscles to keep your body stable.",
            "5. Slowly pull your body upwards, using your back and arm muscles, until your chin is just above the bar.",
            "6. Lower yourself back down in a controlled manner until your arms are straight again."     
        ],
        "image_path": "Images/pull-up.png"      
    },
    
    {
        "Name": "Hip Hinge",
        "Description": "Lower Body Mobility Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Core", "Hamstrings", "Glutes"],
        "Instructions": [
            "1. Stand with your feet shoulder-width apart.",
            "2. Push your hips back while letting your chest come forward (Like you're about to see in a chair).",
            "3. Keep your chest upright and your back straight.", 
            "4. Return to the starting position by pushing with your hips."
        ],
        "image_path": "Images/hip_hinge.png"    
    },
    
    {
        "Name": "Trunk Rotation",
        "Description": "Upper Body Mobility Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Core"],
        "Instructions": [
            "1. Sit or stand with your back straight and your feet shoulder-width apart.",
            "2. Place your hands on your shoulders or extend your arms out in front of you.",
            "3. Slowly rotate your upper body to the right, keeping your hips facing forward.",
            "4. Hold the position for a moment, then rotate back to the center.",
            "5. Repeat the movement to the left side."
        ],
        "image_path": "Images/rotation.png"    
    },
    
    {
        "Name": "Seated Leg Kick",
        "Description": "Lower Body Strengthening Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Quads, Hip Flexors"],
        "Instructions": [
            "1. Sit on a chair with your feet flat on the ground.",
            "2. Lift one leg straight out in front of you.",
            "3. Hold for 2-3 seconds, and the lower it back down.",
            "4. Repeat with the other leg."
        ],
        "image_path": "Images/leg extension.png"            
    },
    
    {
        "Name": "Arm Circles",
        "Description": "Upper Body Mobility Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Shoulders", "Upper Back"],
        "Instructions": [
            "1. Stand or sit with your feet shoulder-width apart.",
            "2. Extend your arms out to the sides at shoulder height.",
            "3. Make small circles with your arms.",
            "4. Gradually make the circles larger."
        ],
        "image_path": "Images/arm_circles.png"         
    },
    
    {
        "Name": "Marching in Place",
        "Description": "Cardiovascular Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Quads", "Hip Flexors", "Core"],
        "Instructions": [
            "1. Stand or sit with your feet shoulder-width apart.",
            "2. Lift one knee up towards your chest.",
            "3. Lower it back down and lift the other knee.",
            "4. Ensure you keep your body upright throughout."
        ],
        "image_path": "Images/marching.png"         
    },
    
    {
        "Name": "Heel Raises",
        "Description": "Cardiovascular Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Calves"],
        "Instructions": [
            "1. Stand or sit with your feet shoulder-width apart.",
            "2. Raise your heels off the ground as high as possible.",
            "3. Lower them back down and repeat"
        ],
        "image_path": "Images/heel raise.png"          
    },
    
    {
        "Name": "OverHead Press",
        "Description": "Upper Body Strengthening Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Shoulders", "Triceps"],
        "Instructions": [
            "1. Stand or sit with your feet slightly more than shoulder-width apart.",
            "2. You can use light weights or no weights for this exercise.",
            "3. Push your arms up towards the sky.",
            "4. Lower your arms back down and repeat."
        ],
        "image_path": "Images/shoulder press.png"
    },
    
    {
        "Name": "Gripping",
        "Description": "Grip Strength",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Fingers, Hand", "Arm"],
        "Instructions": [
            "1. You can use a ball, putty, or anything that can be squeezed.",
            "2. Grab the object with your hand.",
            "3. Give the object a firm squeeze and release.",
            "4. Repeat until time is up."
        ],
        "image_path": "Images/ball_squeeze.png"
    },
    
    {
        "Name": "Sit to Stand",
        "Description": "Lower Body Strengthening Movement",
        "Duration": 30,
        "Difficulty": "Medium",
        "Muscle Groups": ["Quads", "Glutes"],
        "Instructions": [
            "1. Start off in a seated position on a sturdy chair.",
            "2. Have both arms crossed over your body or out in front of you.",
            "3. Lean your chest forward while keeping your back strength to stand up.",
            "4. Push your hips back down into the chair to sit back down.",
            "5. Use the handles of the chair for support if needed."
        ],
        "image_path": "Images/sit_to_stand.png"
    },
    
    {
        "Name": "Side Leg Raise",
        "Description": "Lower Body Strengthening Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Glutes", "Hip"],
        "Instructions": [
            "1. Position yourself next to a counter or behind a stable chair you can hold.",
            "2. Hold the surface for support and shift your weight to your left side.",
            "3. Try to keep your body upright without leaning.",
            "4. Lift your right leg out to the side, keeping your hips and feet pointing forward.",
            "5. Hold briefly before slowly relaxing your leg back to the starting position.",
            "6. Repeat and do the same on the left leg."
        ],
        "image_path": "Images/side_lr.png"
    },
    
    {
        "Name": "Wrist Stretch",
        "Description": "Upper Body Mobility Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Arms", "Wrist"],
        "Instructions": [
            "1. Position yourself in a standing or sitting position.",
            "2. Extend your left arm in front of you with your palm facing away.",
            "3. With your right arm, pull the fingers on your left hand gently, while keeping it straight.",
            "4. Hold the stretch for about 30 seconds.",
            "5. Now position your left hand pointing down so your fingers are pointing towards the ground.",
            "6. Use your right hand to push your fingers towards you gently to feel a stretch at the top of your left wrist.",
            "7. Hold for 30 seconds.",
            "8. Repeat the same steps for the right arm now."
        ],
        "image_path": "Images/wrist_strx.png"
    },
    
    {
        "Name": "Wrist Circles",
        "Description": "Upper Body Mobility Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Wrist"],
        "Instructions": [
            "1. Start in a standing or sitting position.",
            "2. Extend both arms out in front of you or to the side.",
            "3. Keeping your arms straight, draw little circles by moving your wrists/hands in a circle.",
            "4. Gradually make the circles bigger.",
            "5. Reverse the direction after doing 30."
        ],
        "image_path": "Images/wrist_circ.png"
    },
    {
        "Name": "Seated Hamstring Stretch",
        "Description": "Lower Body Mobility Movement",
        "Duration": 30,
        "Difficulty": "Easy",
        "Muscle Groups": ["Hamstrings"],
        "Instructions": [
            "1. Start in a seated position.",
            "2. Sit a little closer to the edge of the chair.",
            "3. Extend your right leg straight while keeping the other leg bent.",
            "4. Lean your chest forward until you feel a stretch behind the leg.",
            "5. Hold for 30 seconds.",
            "6. Repeat on the other leg."
        ],
        "image_path": "Images/hamstring_strx.png"
    }
]



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/exercises/<int:exercise_id>')
def exercise(exercise_id):
    if 1 <= exercise_id <= len(exercises):
        exercise_data = exercises[exercise_id - 1]
    else:
        exercise_data = {
            'Name': 'Exercise Not Found',
            'Description': 'Sorry, this exercise does not exist.',
            'Instructions': [],
            'image_path': ''
        }
        
    previous_id = exercise_id - 1 if exercise_id > 1 else None
    next_id = exercise_id + 1 if exercise_id < len(exercises) else None
    
    return render_template('exercises.html',
                           exercise=exercise_data,
                           previous_id=previous_id,
                           next_id=next_id)

@app.route('/nutrition')
def macronutrients():
    return render_template('macronutrients.html', macronutrients=macronutrients_data)   
    
@app.route('/macrocalculator', methods=['GET', 'POST'])
def macrocalculator():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        activity_level = request.form['activity_level']
        goal = request.form['goal']
        weight_unit = request.form['weight_unit']
        height_unit = request.form['height_unit']

        macros = calculate_macros(weight, height, age, gender, activity_level, goal, weight_unit, height_unit)
        return render_template('macroscalc.html', macros=macros, weight=weight, height=height, age=age, gender=gender, activity_level=activity_level, goal=goal, weight_unit=weight_unit, height_unit=height_unit)

    return render_template('macroscalc.html')



@app.route('/faq')
def faq():
    return render_template('FAQ.html', faq_data=faq_data)

if __name__ == '__main__':
    app.run(debug=True)