from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)