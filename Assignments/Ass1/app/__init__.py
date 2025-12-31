from flask import Flask

def create_app():
    app = Flask(__name__)

    app.secret_key = "supersecrete"

    from app.routes.auth import auth_bp
    from app.routes.reg import reg_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(reg_bp)

    return app