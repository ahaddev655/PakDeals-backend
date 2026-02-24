from flask import request, jsonify

class AdController:
    # ==================== FETCH ALL ADS ====================
    @staticmethod
    def fetchAllAds():
        try:
            print()
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500