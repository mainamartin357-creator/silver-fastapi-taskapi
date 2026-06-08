from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Simple root route
@app.route("/")
def home():
    return {"message": "Task Management API is running (Flask)"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
