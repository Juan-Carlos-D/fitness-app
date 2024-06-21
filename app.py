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
        "image_path": "static/Images/push-up.png"
    },
    
    {
        
    }
]



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/first-exercise')
def first_exercise():
    return render_template('first_exercise.html')

if __name__ == '__main__':
    app.run(debug=True)