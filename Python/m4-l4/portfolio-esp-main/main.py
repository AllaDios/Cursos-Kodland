# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Proyectos y sus URLs
projects = {
    'button_python': 'https://github.com/tuuser/python-project',
    'button_discord': 'https://github.com/AllaDios/EcoBot-Discord',
    'button_html': 'https://github.com/AllaDios/apple-website-clone',
    'button_db': 'https://github.com/tuuser/database-project'
}

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    for button_name in projects.keys():
        if request.form.get(button_name):
            return redirect(projects[button_name])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
