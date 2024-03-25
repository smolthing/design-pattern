-- docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 mysql
-- docker exec -it mysql-container mysql -u root -ppassword

CREATE DATABASE shop_service;
SHOW DATABASE;
/*
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shop_service       |
| sys                |
+--------------------+
*/
USE shop_service;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

ALTER TABLE users ADD UNIQUE (name);
ALTER TABLE users ADD COLUMN email VARCHAR(255) NOT NULL;

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY ,
    user_id INT,
    product_id INT,
    quantity INT
);

SHOW TABLES;
/*
+------------------------+
| Tables_in_shop_service |
+------------------------+
| orders                 |
| users                  |
+------------------------+
*/
INSERT INTO users (name, email) VALUES("bibi", "bibi@bibi.com");
INSERT INTO users (name, email) VALUES("dudu", "dudu@dudu.com");

UPDATE users SET name="bibi1", email="bibi1@bibi.com" WHERE name="bibi";
SELECT name from users;


INSERT INTO orders (user_id, product_id, quantity) VALUES(1,1,1);
INSERT INTO orders (user_id, product_id, quantity) VALUES(1,1,2);
INSERT INTO orders (user_id, product_id, quantity) VALUES(2,2,2);
INSERT INTO orders (user_id, product_id, quantity) VALUES(3,3,3);

SELECT DISTINCT product_id FROM users AS u LEFT JOIN orders AS o ON u.id=o.user_id WHERE u.id=1;
SELECT DISTINCT product_id, SUM(quantity) as total_quantity 
    FROM users AS u
    LEFT JOIN orders AS o
    ON u.id=o.user_id
    WHERE u.id=1
    GROUP BY o.product_id;
/*
+------------+
| product_id |
+------------+
|          1 |
+------------+

+------------+----------------+
| product_id | total_quantity |
+------------+----------------+
|          1 |              3 |
+------------+----------------+
*/


SELECT o.product_id FROM users u LEFT JOIN orders o ON  u.id=o.user_id;

SELECT id FROM users LIMIT 1 OFFSET 1;

SELECT GROUP_CONCAT(o.id ORDER BY o.id SEPARATOR ',') AS order_ids FROM users u JOIN orders o ON u.id = o.user_id GROUP BY u.name;


DELETE FROM users where id=1;
DROP TABLE users;


