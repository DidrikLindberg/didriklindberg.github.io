"""Flask application factory."""
from flask import Flask

from config.settings import Config


def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    from app.api import routes as api_routes

    app.register_blueprint(api_routes.bp)

    # Health check endpoint
    @app.route("/health")
    def health():
        return {"status": "healthy"}, 200

    return app
