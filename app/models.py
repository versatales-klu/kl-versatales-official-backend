from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

# app/models.py

from app import db
from app.utils import get_current_time  # If you want to use timestamps (optional)


# ✅ RoleRegistrations model
class RoleRegistrations(db.Model):
    _tablename_ = 'RoleRegistrations'  # Use _tablename_ not tablename

    id = db.Column(db.Integer, primary_key=True)
    college_id  = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    dept = db.Column(db.String(100), nullable=False)
    wingname = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.String(255), nullable=True)
    experience = db.Column(db.String(255), nullable=True)

    def _repr_(self):
        return f"<RoleRegistrations {self.name} - {self.mail}>"