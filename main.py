from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/testdriver.db'
db = SQLAlchemy(app)

# Definir modelo de base de datos utilizando SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar las credenciales del usuario en la base de datos
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # Iniciar sesión exitosa, redirigir a la página de inicio
            return redirect(url_for('home'))
        else:
            error = 'Credenciales incorrectas. Por favor, inténtalo nuevamente.'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Verificar si el nombre de usuario ya está en uso
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error = 'El nombre de usuario ya está en uso. Por favor, elige otro.'
            return render_template('register.html', error=error)
        
        # Verificar si las contraseñas coinciden
        if password != confirm_password:
            error = 'Las contraseñas no coinciden. Por favor, inténtalo nuevamente.'
            return render_template('register.html', error=error)
        
        # Crear un nuevo usuario en la base de datos
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        # Registro exitoso, redirigir a la página de inicio de sesión
        return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
