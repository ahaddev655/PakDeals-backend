from flask import request, jsonify
from ..models.ad_models import Ad

class AdController:
    # ==================== FETCH ALL ADS ====================
    @staticmethod
    def fetchAllAds():
        try:
            all_ads = Ad.fetch_ads_()
            expired_ads = Ad.expired_ads_()
            active_ads = Ad.active_ads_()
            pending_ads = Ad.pending_ads_()
            
            return jsonify({"message": "Ads fetched successfully", "all_ads": all_ads, "expired_ads": expired_ads, "pending_ads": pending_ads, "active_ads": active_ads}), 201
            
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500
        
    # ==================== FETCH USER ADS ====================
    def fetchUserAds(id):
        try:
            all_user_ads = Ad.fetch_ads_by_id(id)
            
            return jsonify({"message": "Ads fetched successfully", "all_ads": all_user_ads}), 201
            
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500
        
    # ==================== DELETE USER ADS ====================
    def deleteUserAd(id):
        try:
            all_ads = Ad.fetch_ads_by_id(id)
            
            if len(all_ads):
                return jsonify({"error": "Ad not found",}), 400
            
            Ad.delete_ad_by_id(ad_id=id)
            
            return jsonify({"message": "Ad deleted successfully",}), 201
            
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500