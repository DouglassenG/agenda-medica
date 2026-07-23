from flask import Flask
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

    from app.models import init_db
    init_db()

    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app