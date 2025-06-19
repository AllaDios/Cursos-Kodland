from flask import Flask
from random import choice

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
]

@app.route("/")
def index():
    return f'''
        <h1>Hola Bienvenido a Consejos.com</h1>
        <p>¡Haz clic en el enlace para ver un dato aleatorio!</p>
        <a href="/fact_random">Ver más consejos</a>
        <a href="/secret_page">Página secreta</a>
    '''

@app.route("/fact_random")
def random_dact():
    return f'''
        <h1>Dato aleatorio</h1>
        <p>{choice(facts_list)}</p>
        <a href="/">Volver a la página principal</a>

    '''

@app.route("/secret_page")
def generate_password():
    pass_length = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
    password = "".join(choice(characters) for _ in range(pass_length))
    return f'''
        <h1>¡Bienvenido a la página secreta!</h1>
        <h1>Tu contraseña generada es:</h1>
        <input type="num" value="{password}" readonly>
        <p>{password}</p>
        <a href="/">Volver a la página principal</a>
    '''

app.run(debug=True)