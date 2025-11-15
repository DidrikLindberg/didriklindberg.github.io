"""API routes."""
from flask import Blueprint, jsonify

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/")
def index():
    """API root endpoint."""
    return jsonify({"message": "Welcome to the API", "version": "1.0.0"})


@bp.route("/hello/<name>")
def hello(name):
    """Sample endpoint with parameter."""
    return jsonify({"message": f"Hello, {name}!"})
