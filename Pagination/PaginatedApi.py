from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'your_database_name',
}

# Connect to MySQL
connection = mysql.connector.connect(**db_config)

# API endpoint for paginated products
@app.route('/api/products', methods=['GET'])
def get_paginated_products():
    try:
        page_number = int(request.args.get('page', 1)) - 1  # Adjusting page number to 0-based index
        page_size = int(request.args.get('size', 10))

        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM products LIMIT %s OFFSET %s', (page_size, page_number * page_size))
        products = cursor.fetchall()
        cursor.close()

        return jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
