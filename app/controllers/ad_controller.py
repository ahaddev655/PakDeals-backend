from flask import request, jsonify
from ..models.ad_models import Ad
import cloudinary.uploader
import json
from app.database.db import get_connection


class AdController:
    # ==================== FETCH ALL ADS ====================
    @staticmethod
    def fetchAllAds():
        try:
            all_ads = Ad.fetch_ads_()
            expired_ads = Ad.expired_ads_()
            active_ads = Ad.active_ads_()
            pending_ads = Ad.pending_ads_()

            return (
                jsonify(
                    {
                        "message": "Ads fetched successfully",
                        "all_ads": all_ads,
                        "expired_ads": expired_ads,
                        "pending_ads": pending_ads,
                        "active_ads": active_ads,
                    }
                ),
                201,
            )

        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500

    # ==================== FETCH USER ADS ====================
    @staticmethod
    def fetchUserAds(id):
        try:
            all_user_ads = Ad.fetch_ads_by_id(id)

            return (
                jsonify(
                    {"message": "Ads fetched successfully", "all_ads": all_user_ads}
                ),
                201,
            )

        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500

    # ==================== DELETE USER ADS ====================
    @staticmethod
    def deleteUserAd(id):
        try:
            all_ads = Ad.fetch_ads_by_id(id)

            if len(all_ads) == 0:
                return jsonify({"error": "Ad not found"}), 400

            Ad.delete_ad_by_id(ad_id=id)

            return (
                jsonify(
                    {
                        "message": "Ad deleted successfully",
                    }
                ),
                201,
            )

        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500

    # ==================== ADD ANIMAL AD ====================
    @staticmethod
    def addAnimalAd(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE id = %s", (id,))
            if not cursor.fetchone():
                return jsonify({"error": f"user_id {id} does not exist"}), 400

            subCategory = request.form.get("subCategory")
            type = request.form.get("type")
            sex = request.form.get("sex")
            vaccinationStatus = request.form.get("vaccinationStatus")
            location = request.form.get("location")
            adTitle = request.form.get("adTitle")
            description = request.form.get("description")
            price = request.form.get("price")
            sellerName = request.form.get("sellerName")
            sellerContact = request.form.get("sellerContact")
            features = request.form.get("features")
            breed = request.form.get("breed")
            age = request.form.get("age")
            color = request.form.get("color")

            images = request.files.getlist("images")

            uploaded_urls = []
            for image in images:
                result = cloudinary.uploader.upload(image)
                uploaded_urls.append(result["secure_url"])
            images_json = json.dumps(uploaded_urls)

            last_id = Ad.add_animal_ad(
                subCategory,
                type,
                sex,
                vaccinationStatus,
                location,
                features,
                breed,
                age,
                color,
                images_json,
                id,
                adTitle,
                description,
                price,
                sellerName,
                sellerContact,
            )

            cursor.close()
            conn.close()
            return (
                jsonify({"message": "Ad created successfully", "ad_id": last_id}),
                201,
            )

        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500

    # ==================== ADD BIKE AD ====================
    @staticmethod
    def addBikeAd(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE id = %s", (id,))
            if not cursor.fetchone():
                return jsonify({"error": f"user_id {id} does not exist"}), 400

            subCategory = request.form.get("subCategory")
            make = request.form.get("make")
            engineType = request.form.get("engineType")
            engineCapacity = request.form.get("engineCapacity")
            ignitionType = request.form.get("ignitionType")
            origin = request.form.get("origin")
            condition = request.form.get("condition")
            registrationCity = request.form.get("registrationCity")
            location = request.form.get("location")
            adTitle = request.form.get("adTitle")
            description = request.form.get("description")
            price = request.form.get("price")
            sellerName = request.form.get("sellerName")
            sellerContact = request.form.get("sellerContact")
            features = request.form.get("features")
            model = request.form.get("model")
            year = request.form.get("year")
            kmDriven = request.form.get("kmDriven")

            images = request.files.getlist("images")

            uploaded_urls = []
            for image in images:
                result = cloudinary.uploader.upload(image)
                uploaded_urls.append(result["secure_url"])
            images_json = json.dumps(uploaded_urls)

            last_id = Ad.add_bike_ad(
                id,
                subCategory,
                make,
                engineType,
                engineCapacity,
                ignitionType,
                origin,
                condition,
                registrationCity,
                location,
                adTitle,
                description,
                price,
                sellerName,
                sellerContact,
                features,
                model,
                year,
                kmDriven,
                images_json,
            )

            cursor.close()
            conn.close()
            return (
                jsonify({"message": "Ad created successfully", "ad_id": last_id}),
                201,
            )

        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500
