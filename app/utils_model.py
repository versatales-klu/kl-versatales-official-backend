from app import db
from app.models import ClubRoleRegistration

def check_registration_status(mail):
    return db.session.query(
        db.exists().where(ClubRoleRegistration.mail == mail)
    ).scalar()

def add_role_registration(college_id, name, mail, year, gender, dept, wingname, reason=None, experience=None):
    try:
        new_entry = ClubRoleRegistration(
            college_id=college_id,
            name=name,
            mail=mail,
            year=year,
            gender=gender,
            dept=dept,
            wingname=wingname,
            reason=reason,
            experience=experience
        )
        db.session.add(new_entry)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Error adding role registration: {e}")
        return False
