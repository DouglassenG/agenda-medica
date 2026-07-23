from flask import Flask, send_from_directory
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

    @app.route("/public/<path:filename>")
    def public_files(filename):
        return send_from_directory("../public", filename)

    from app.models import init_db
    init_db()

    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app