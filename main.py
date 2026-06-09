from flask import Flask
from models import db
from routes.tasks import tasks_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprint
app.register_blueprint(tasks_bp, url_prefix='/tasks')

@app.route("/")
def home():
    return {"message": "Task Management API is running (Flask)"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables
    app.run(host="0.0.0.0", port=8000, debug=True)
