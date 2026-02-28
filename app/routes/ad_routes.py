from flask import Blueprint
from ..controllers.ad_controller import AdController

ad_bp = Blueprint("ads", __name__, url_prefix="/api/ads")

ad_bp.route("/all-ads", methods=["GET"])(AdController.fetchAllAds)

ad_bp.route("/all-user-ads/<int:id>", methods=["GET"])(AdController.fetchUserAds)

ad_bp.route("/delete-user-ad/<int:id>/<string:table_name>", methods=["DELETE"])(AdController.deleteUserAd)

# ==================== ADS ROUTES ====================

# -------------------- ANIMAL AD --------------------
ad_bp.route("/add-animal-ad/<int:id>", methods=["POST"])(AdController.addAnimalAd)

# -------------------- BIKE AD --------------------
ad_bp.route("/add-bike-ad/<int:id>", methods=["POST"])(AdController.addBikeAd)

# -------------------- BOOKS AD --------------------
ad_bp.route("/add-book-ad/<int:id>", methods=["POST"])(AdController.addBookAd)

# -------------------- ELECTRONICS AD --------------------
ad_bp.route("/add-electronics-ad/<int:id>", methods=["POST"])(AdController.addElectronicsAd)

# -------------------- FASHION AD --------------------
ad_bp.route("/add-fashion-ad/<int:id>", methods=["POST"])(AdController.addFashionAd)

# -------------------- FURNITURE AD --------------------
ad_bp.route("/add-furniture-ad/<int:id>", methods=["POST"])(AdController.addFurnitureAd)

# -------------------- KIDS AD --------------------
ad_bp.route("/add-kids-ad/<int:id>", methods=["POST"])(AdController.addKidsAd)
