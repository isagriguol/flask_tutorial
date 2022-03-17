from datetime import datetime
from flaskblog import db

# se decalaram os modelos depois de criar a db para não gerar um erro em círculos

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# o user tem um ID único
	username = db.Column(db.String(20), unique=True, nullable=False)
	# 20 é o limite de caracteres
	# unique=True significa que deve ser um único argumento
	# nullable=False significa que o campo deve ser preenchido
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)
	# constrói uma relação com o model Post
	# atributo lazy: atua na inserção do dado na base de dados
	# lazy=True signfica que o SQLAlchemy vai reunir os posts de um mesmo user

	def __repr__(self): # o método com __ determina como o objeto é mostrado
		return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	# identifica o post ao seu respectivo user

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"
