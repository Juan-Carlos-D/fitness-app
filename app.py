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

if __name__ == '__main__':
    app.run(debug=True)