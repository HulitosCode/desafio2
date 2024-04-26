from app import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/desafio2"

# Inicialização da extensão SQLAlchemy
db = SQLAlchemy(app)
app.secret_key = "secret_key"

