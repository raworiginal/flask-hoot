from flask import Flask
from dotenv import load_dotenv
from auth_blueprint import authentication_blueprint
from hoots_blueprint import hoots_blueprint
from comments_blueprints import comments_blueprint

load_dotenv()

app = Flask(__name__)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(hoots_blueprint)
app.register_blueprint(comments_blueprint)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
