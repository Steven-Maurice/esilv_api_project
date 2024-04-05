from flask import Flask
from function_get_data import get_data

app = Flask(__name__)

app.register_blueprint(get_data)

if __name__ == '__main__':
    app.run(debug=True)