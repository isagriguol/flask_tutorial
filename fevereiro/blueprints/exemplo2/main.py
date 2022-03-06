from flask import Flask
from my_application.index import index_bp
from my_application.login import login_bp

app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)

if __name__ == '__main__':
	app.run(debug=True)