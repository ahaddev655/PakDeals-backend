from flask import Flask
from flask_bcrypt import Bcrypt
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp
from app.routes.ad_routes import ad_bp
from app.assets.create_tables import Tables
from flask_cors import CORS
from dotenv import load_dotenv
import cloudinary
import os

bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv()
    bcrypt.init_app(app)

    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    )

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(ad_bp)

    with app.app_context():
        Tables.create_users_table()
        Tables.create_animals_ads_table()
        Tables.create_bikes_ads_table()
        Tables.create_books_ads_table()
        Tables.create_electronics_ads_table()
        Tables.create_fashion_ads_table()
        Tables.create_furniture_ads_table()
        Tables.create_kids_ads_table()
        Tables.create_mobile_ads_table()
        Tables.create_motors_ads_table()
        Tables.create_property_sale_ads_table()
        Tables.create_property_rent_ads_table()

    return app
