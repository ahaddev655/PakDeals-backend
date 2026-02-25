from flask import Blueprint
from ..controllers.ad_controller import AdController

ad_bp = Blueprint("ads", __name__, url_prefix="/api/ads")

ad_bp.route("/all-ads", methods=["GET"])(AdController.fetchAllAds)
ad_bp.route("/all-user-ads/<int:id>", methods=["GET"])(AdController.fetchUserAds)
ad_bp.route("/delete-user-ad/<int:id>", methods=["DELETE"])(AdController.deleteUserAd)

# ==================== ADS ROUTES ====================
# -------------------- ANIMAL AD --------------------
ad_bp.route("/add-animal-ad/<int:id>", methods=["POST"])(AdController.addAnimalAd)
ad_bp.route("/add-bike-ad/<int:id>", methods=["POST"])(AdController.addBikeAd)
