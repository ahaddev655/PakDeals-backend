from app.database.db import get_connection


class Tables:

    # ==================== USER TABLE ====================
    def create_users_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                firstName VARCHAR(50) NOT NULL,
                lastName VARCHAR(50) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                token VARCHAR(255) NOT NULL,
                is_google_user BOOLEAN DEFAULT FALSE,
                mobileNumber VARCHAR(255) DEFAULT NULL,
                country VARCHAR(255) DEFAULT NULL,
                city VARCHAR(255) DEFAULT NULL,
                address VARCHAR(255) DEFAULT NULL,
                company VARCHAR(255) DEFAULT NULL,
                description VARCHAR(255) DEFAULT NULL,
                buisnessCategory VARCHAR(255) DEFAULT NULL,
                buisnessType VARCHAR(255) DEFAULT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()

    # ==================== ANIMAL ADS TABLE ====================
    def create_animals_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS animal_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                sex VARCHAR(255) NOT NULL,
                vaccinationStatus VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                breed VARCHAR(255) NOT NULL,
                age VARCHAR(50) NOT NULL,
                color VARCHAR(100) NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()

    # ==================== BIKES ADS TABLE ====================
    def create_bikes_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bikes_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                make VARCHAR(255) NOT NULL,
                engineType VARCHAR(255) NOT NULL,
                engineCapacity VARCHAR(255) NOT NULL,
                ignitionType VARCHAR(255) NOT NULL,
                origin VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                registrationCity VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                model VARCHAR(255) NOT NULL,
                year VARCHAR(50) NOT NULL,
                kmDriven VARCHAR(100) NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()

    # ==================== BOOKS ADS TABLE ====================
    def create_books_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                itemType VARCHAR(255) NOT NULL,
                language VARCHAR(255) NOT NULL,
                format VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                genre VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()

    # ==================== ELECTRONICS ADS TABLE ====================
    def create_electronics_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS electronics_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                brand VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                warranty VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                type VARCHAR(255) NOT NULL,
                model VARCHAR(255) NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()

    # ==================== FASHION ADS TABLE ====================
    def create_fashion_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fashion_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                brand VARCHAR(255) NOT NULL,
                gender VARCHAR(255) NOT NULL,
                size VARCHAR(255) NOT NULL,
                material VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                color VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()

    # ==================== FURNITURE ADS TABLE ====================
    def create_furniture_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS furniture_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                itemType VARCHAR(255) NOT NULL,
                material VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                brand VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()
        
    # ==================== KIDS ADS TABLE ====================
    def create_kids_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS kids_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                itemType VARCHAR(255) NOT NULL,
                ageGroup VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                brand VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()
        
    # ==================== MOBILES ADS TABLE ====================
    def create_mobile_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mobile_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                brand VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()
        
    # ==================== MOTORS ADS TABLE ====================
    def create_motors_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS motors_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                make VARCHAR(255) NOT NULL,
                `condition` VARCHAR(255) NOT NULL,
                bodyFuel VARCHAR(255) NOT NULL,
                transmisson VARCHAR(255) NOT NULL,
                bodyType VARCHAR(255) NOT NULL,
                documentStatus VARCHAR(255) NOT NULL,
                assembly VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                carColor VARCHAR(255) NOT NULL,
                carYear VARCHAR(255) NOT NULL,
                owners VARCHAR(255) NOT NULL,
                seats VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()

    # ==================== PROPERTY RENT ADS TABLE ====================
    def create_property_rent_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS property_rent_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                areaUnit VARCHAR(255) NOT NULL,
                areaSize VARCHAR(255) NOT NULL,
                furnishedStatus VARCHAR(255) NOT NULL,
                bedrooms VARCHAR(255) NOT NULL,
                bathrooms VARCHAR(255) NOT NULL,
                numberOfStoreys VARCHAR(255) NOT NULL,
                constructionState VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()
        
    # ==================== PROPERTY SALE ADS TABLE ====================
    def create_property_sale_ads_table():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS property_sale_ads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                subCategory VARCHAR(255) NOT NULL,
                areaUnit VARCHAR(255) NOT NULL,
                area VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                adTitle VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sellerName VARCHAR(255) NOT NULL,
                sellerContact VARCHAR(255) NOT NULL,
                features TEXT NOT NULL,
                images TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                isActive BOOLEAN DEFAULT FALSE,
                isSold BOOLEAN DEFAULT FALSE,
                isExpired BOOLEAN DEFAULT FALSE,
                isFeatured BOOLEAN DEFAULT FALSE,
                payment_due_at TIMESTAMP NULL DEFAULT NULL,
                isPending BOOLEAN DEFAULT TRUE,
                
                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """)
        connection.commit()
        cursor.close()
        connection.close()