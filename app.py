from flask import Flask, render_template, request, url_for
from faq import faq_data 
from macronutrients import macronutrients_data
from macroscalc import calculate_macros
from exercises import exercises
from blogs import blogs
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/beginner-program')
def beginner_program():
    return render_template('beginner_program.html')


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

# Route to display all blog posts
@app.route('/blogs')
def all_blogs():
    return render_template('blogs.html', blogs=blogs)

def process_content(content):
    # Find all occurrences of {{ url_for(...)}}
    matches = re.findall(r"\{\{\s*url_for\([^)]+\)\s*\}\}", content)
    for match in matches:
        # Evaluate the url_for expression
        evaluated_url = eval(match.strip("{{}}"))
        # Replace the url_for expression with the actual URL
        content = content.replace(match, evaluated_url)
    return content

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog = next((blog for blog in blogs if blog['id'] == blog_id), None)
    if blog:
        blog['content'] = process_content(blog['content'])
        return render_template('blog.html', blog=blog)
    else:
        return 'Blog not found', 404
def render_program(title, main_title, intro_image, intro_text, intro_subtext, download_link, goals, goals_title, download_section_title, background_image):
    return render_template(
        'program_base.html',
        title=title,
        main_title=main_title,
        intro_image=intro_image,
        intro_text=intro_text,
        intro_subtext=intro_subtext,
        download_link=download_link,
        goals=goals,
        goals_title=goals_title,
        download_section_title=download_section_title,
        background_image=background_image
    )
    
@app.route('/program/<program_name>')
def program(program_name):
    program_data = {
        "beginner_program": {
            "title": "Beginner Program",
            "main_title": "Welcome to the Beginner Program!",
            "intro_image": url_for('static', filename='Images/gym_s2.png'),
            "intro_text": "This program is designed to help you get started with calisthenics. It includes essential exercises and routines that will build your strength, flexibility, and endurance.",
            "intro_subtext": "You can download the complete exercise program in PDF format by clicking the button below.",
            "download_link": "#",
            "goals": [
                {"image": "#", "description": "Description of Goal 1"},
                {"image": "#", "description": "Description of Goal 2"},
                {"image": "#", "description": "Description of Goal 3"}
            ],
            "goals_title": "This program's goals are",
            "download_section_title": "Download Section",
            "background_image": url_for('static', filename='Images/gym_s2.png')
        },
        "muscleup_program": {
            "title": "Muscle-Up Program",
            "main_title": "Welcome to the Muscle-Up Program!",
            "intro_image": "#",
            "intro_text": "This program is designed to help you achieve your first muscle-up. It includes essential exercises and routines that will build your upper body strength and technique.",
            "intro_subtext": "You can download the complete exercise program in PDF format by clicking the button below.",
            "download_link": "#",
            "goals": [
                {"image": "#", "description": "Description of Muscle-Up Goal 1"},
                {"image": "#", "description": "Description of Muscle-Up Goal 2"},
                {"image": "#", "description": "Description of Muscle-Up Goal 3"}
            ],
            "goals_title": "This program's goals are",
            "download_section_title": "Download Section",
            "background_image": "#"
        }
        # Add more programs here as needed
    }

    if program_name in program_data:
        return render_program(**program_data[program_name])
    else:
        return "Program not found", 404

if __name__ == '__main__':
    app.run(debug=True)