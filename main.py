from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/testdriver.db'; # local database.
db = SQLAlchemy(app)

# Definir modelos de base de datos utilizando SQLAlchemy
# Ejemplo:
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     .....

@app.route('/')
def home():
    return render_template('index.html')

# Agrega más rutas y funciones de vista según tus necesidades

if __name__ == '__main__':
    app.run(debug=True)
