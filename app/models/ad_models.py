from app.database.db import get_connection
import pymysql
from datetime import datetime, timedelta


class Ad:
    # ==================== TOTAL AD COUNT ====================
    @staticmethod
    def fetch_ads_():
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT 
            (SELECT COUNT(*) FROM animal_ads) +
            (SELECT COUNT(*) FROM bikes_ads) +
            (SELECT COUNT(*) FROM electronics_ads) +
            (SELECT COUNT(*) FROM fashion_ads) +
            (SELECT COUNT(*) FROM furniture_ads) +
            (SELECT COUNT(*) FROM kids_ads) +
            (SELECT COUNT(*) FROM mobile_ads) +
            (SELECT COUNT(*) FROM motors_ads) +
            (SELECT COUNT(*) FROM property_rent_ads) +
            (SELECT COUNT(*) FROM property_sale_ads)
        AS total_ads
        """

        cursor.execute(sql)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result["total_ads"]

    # ==================== EXPIRED AD COUNT ====================
    @staticmethod
    def expired_ads_():
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT 
            (SELECT COUNT(*) FROM animal_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM bikes_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM electronics_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM fashion_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM furniture_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM kids_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM mobile_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM motors_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM property_rent_ads WHERE isExpired = TRUE) +
            (SELECT COUNT(*) FROM property_sale_ads WHERE isExpired = TRUE)
        AS expired_ads
        """

        cursor.execute(sql)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result["expired_ads"]

    # ==================== ACTIVE AD COUNT ====================
    @staticmethod
    def active_ads_():
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT 
            (SELECT COUNT(*) FROM animal_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM bikes_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM electronics_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM fashion_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM furniture_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM kids_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM mobile_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM motors_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM property_rent_ads WHERE isActive = TRUE) +
            (SELECT COUNT(*) FROM property_sale_ads WHERE isActive = TRUE)
        AS active_ads
        """

        cursor.execute(sql)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result["active_ads"]

    # ==================== PENDING AD COUNT ====================
    @staticmethod
    def pending_ads_():
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT 
            (SELECT COUNT(*) FROM animal_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM bikes_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM electronics_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM fashion_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM furniture_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM kids_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM mobile_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM motors_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM property_rent_ads WHERE isPending = TRUE) +
            (SELECT COUNT(*) FROM property_sale_ads WHERE isPending = TRUE)
        AS pending_ads
        """

        cursor.execute(sql)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result["pending_ads"]

    # ==================== AD FETCHED BY ID ====================
    def fetch_ads_by_id(id):
        conn = get_connection()
        cursor = conn.cursor()

        tables = [
            "animal_ads",
            "bikes_ads",
            "books_ads",
            "electronics_ads",
            "fashion_ads",
            "furniture_ads",
            "kids_ads",
            "mobile_ads",
            "motors_ads",
            "property_rent_ads",
            "property_sale_ads",
        ]

        all_ads = {}

        for table in tables:
            cursor.execute(f"SELECT * FROM {table} WHERE user_id = %s", (id,))
            all_ads[table] = cursor.fetchall()

        cursor.close()
        conn.close()

        return all_ads

    # ==================== AD DELETE BY ID ====================
    def delete_ad_by_id(ad_id, tableName):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {tableName} WHERE id = %s", (ad_id,))
        conn.commit()

        rows_deleted = cursor.rowcount

        cursor.close()
        conn.close()

        return rows_deleted > 0

    # ==================== ADD ANIMAL AD ====================
    def add_animal_ad(
        subCategory,
        type,
        sex,
        vaccinationStatus,
        location,
        features,
        breed,
        age,
        color,
        images,
        id,
        adTitle,
        description,
        price,
        sellerName,
        sellerContact,
    ):

        conn = get_connection()
        cursor = conn.cursor()

        payment_due_at = datetime.now() + timedelta(days=30)

        sql = """
        INSERT INTO animal_ads 

        (user_id, subCategory, type, sex, vaccinationStatus, location,
         adTitle, description, price, sellerName, sellerContact,
         features, breed, age, color, images, payment_due_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            sql,
            (
                id,
                subCategory,
                type,
                sex,
                vaccinationStatus,
                location,
                adTitle,
                description,
                price,
                sellerName,
                sellerContact,
                features,
                breed,
                age,
                color,
                images,
                payment_due_at,
            ),
        )
        conn.commit()
        last_id = cursor.lastrowid

        cursor.close()
        conn.close()
        return last_id

    # ==================== ADD BIKES AD ====================
    def add_bike_ad(
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
        images,
    ):

        conn = get_connection()
        cursor = conn.cursor()

        payment_due_at = datetime.now() + timedelta(days=30)

        sql = """
            INSERT INTO bikes_ads
            (user_id, subCategory, make, engineType, engineCapacity, ignitionType,
             `origin`, `condition`, registrationCity, location, adTitle, description,
             price, sellerName, sellerContact, features, model, year,
             kmDriven, images, payment_due_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

        cursor.execute(
            sql,
            (
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
                images,
                payment_due_at,
            ),
        )
        conn.commit()
        last_id = cursor.lastrowid

        cursor.close()
        conn.close()
        return last_id

    # ==================== ADD BOOKS AD ====================
    def add_books_ad(
        id,
        subCategory,
        itemType,
        language,
        format,
        condition,
        location,
        adTitle,
        description,
        price,
        genre,
        author,
        sellerName,
        sellerContact,
        features,
        images,
    ):

        conn = get_connection()
        cursor = conn.cursor()

        payment_due_at = datetime.now() + timedelta(days=30)

        sql = """
            INSERT INTO books_ads
            (user_id, subCategory, itemType, language, format, `condition`, location, adTitle, description,
             price, genre, author, sellerName, sellerContact, features, images, payment_due_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

        cursor.execute(
            sql,
            (
                id,
                subCategory,
                itemType,
                language,
                format,
                condition,
                location,
                adTitle,
                description,
                price,
                genre,
                author,
                sellerName,
                sellerContact,
                features,
                images,
                payment_due_at,
            ),
        )
        conn.commit()
        last_id = cursor.lastrowid

        cursor.close()
        conn.close()
        return last_id

    # ==================== ADD ELECTRONICS AD ====================
    def add_electronics_ad(
        id,
        subCategory,
        brand,
        warranty,
        condition,
        location,
        adTitle,
        description,
        price,
        sellerName,
        sellerContact,
        features,
        type,
        model,
        images,
    ):

        conn = get_connection()
        cursor = conn.cursor()

        payment_due_at = datetime.now() + timedelta(days=30)

        sql = """
            INSERT INTO electronics_ads
            (user_id, subCategory, brand, `condition`, warranty, location,
             adTitle, description, price, sellerName, sellerContact, features, type,
             model, images, payment_due_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

        cursor.execute(
            sql,
            (
                id,
                subCategory,
                brand,
                condition,
                warranty,
                location,
                adTitle,
                description,
                price,
                sellerName,
                sellerContact,
                features,
                type,
                model,
                images,
                payment_due_at,
            ),
        )
        conn.commit()
        last_id = cursor.lastrowid

        cursor.close()
        conn.close()
        return last_id

    # ==================== ADD FASHION AD ====================
    def add_fashion_ad(
        id,
        subCategory,
        brand,
        gender,
        size,
        material,
        condition,
        type,
        location,
        adTitle,
        description,
        price,
        sellerName,
        sellerContact,
        color,
        features,
        images,
    ):

        conn = get_connection()
        cursor = conn.cursor()

        payment_due_at = datetime.now() + timedelta(days=30)

        sql = """
            INSERT INTO fashion_ads
            (user_id, subCategory, brand, gender, size, material, 
             `condition`, type, location, adTitle, description, color, 
             features, price, sellerName, sellerContact, images, payment_due_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

        cursor.execute(
            sql,
            (
                id,
                subCategory,
                brand,
                gender,
                size,
                material,
                condition,
                type,
                location,
                adTitle,
                description,
                price,
                sellerName,
                sellerContact,
                color,
                features,
                images,
                payment_due_at,
            ),
        )
        conn.commit()
        last_id = cursor.lastrowid

        cursor.close()
        conn.close()
        return last_id

    # ==================== ADD FURNITURE AD ====================
    def add_furniture_ad(
        id,
        subCategory,
        itemType,
        material,
        condition,
        location,
        adTitle,
        description,
        brand,
        dimensions,
        features,
        price,
        sellerName,
        sellerContact,
        images,
    ):

        conn = get_connection()
        cursor = conn.cursor()

        payment_due_at = datetime.now() + timedelta(days=30)

        sql = """
            INSERT INTO furniture_ads
             (user_id, subCategory, itemType, material, `condition`, location,
             adTitle, description, brand, dimensions, features, price,
             sellerName, sellerContact, images, payment_due_at)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

        cursor.execute(
            sql,
            (
                id,
                subCategory,
                itemType,
                material,
                condition,
                location,
                adTitle,
                description,
                brand,
                dimensions,
                features,
                price,
                sellerName,
                sellerContact,
                images,
                payment_due_at,
            ),
        )
        conn.commit()
        last_id = cursor.lastrowid

        cursor.close()
        conn.close()
        return last_id

    # ==================== ADD KIDS AD ====================
    def add_kids_ad(
        id,
        subCategory,
        itemType,
        ageGroup,
        condition,
        location,
        adTitle,
        description,
        brand,
        features,
        price,
        sellerName,
        sellerContact,
        images,
    ):

        conn = get_connection()
        cursor = conn.cursor()

        payment_due_at = datetime.now() + timedelta(days=30)

        sql = """
            INSERT INTO kids_ads
             (user_id, subCategory, itemType, ageGroup, `condition`, location,
             adTitle, description, brand, features, price, sellerName,
             sellerContact, images, payment_due_at)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

        cursor.execute(
            sql,
            (
                id,
                subCategory,
                itemType,
                ageGroup,
                condition,
                location,
                adTitle,
                description,
                brand,
                features,
                price,
                sellerName,
                sellerContact,
                images,
                payment_due_at,
            ),
        )
        conn.commit()
        last_id = cursor.lastrowid

        cursor.close()
        conn.close()
        return last_id
