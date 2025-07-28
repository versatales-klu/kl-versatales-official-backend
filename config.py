import os

# ✅ Supabase direct connection for migrations
SUPABASE_SQLALCHEMY_DATABASE_URI = "postgresql://postgres.nwoiqfdvwzesctgtlrbi:thisisthedatabasepassword@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
DB_PATH = os.path.join(INSTANCE_DIR, 'versatales_official.db')

# ✅ Set the DATABASE_URL environment variable if it's not already set
os.environ.setdefault('DATABASE_URL', SUPABASE_SQLALCHEMY_DATABASE_URI)

# ✅ Ensure FLASK_ENV is set
os.environ.setdefault('FLASK_ENV', 'development')

# ✅ Create the instance folder if it doesn't exist
if not os.path.exists(INSTANCE_DIR):
    os.makedirs(INSTANCE_DIR)

class Config:
    SITE_URL = "https://kl-versatales-official-backend.onrender.com"
    SECRET_KEY = os.environ.get('SECRET_KEY', 'versatales-secret-key')

    if os.environ.get('FLASK_ENV') == 'development':
        print("Local Database Accessing...")
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
    else:
        print("Using Supabase Database")
        SQLALCHEMY_DATABASE_URI = os.environ.get(
            'DATABASE_URL',
            SUPABASE_SQLALCHEMY_DATABASE_URI  # Fallback if env var isn't set
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
