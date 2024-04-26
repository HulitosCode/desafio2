from config.db import db, app
from Entity.Meal import Meal

with app.app_context():
    db.create_all()