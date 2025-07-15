from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category FROM Products")
        products = []
        for row in cursor.fetchall():
            products.append({
                'id': row[0],
                'name': row[1],
                'price': row[2],
                'category': row[3]
            })
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def get_products_from_csv():
    try:
        products = []
        with open('products.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'price': float(row['price']),
                    'category': row['category']
                })
        return products
    except (FileNotFoundError, csv.Error) as e:
        print(f"CSV error: {e}")
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source', 'json').lower()
    product_id = request.args.get('id')

    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                products = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return render_template('product_display.html', error="Error loading JSON data")

    elif source == 'csv':
        products = get_products_from_csv()
        if products is None:
            return render_template('product_display.html', error="Error loading CSV data")

    elif source == 'sql':
        products = get_products_from_db()
        if products is None:
            return render_template('product_display.html', error="Error loading database data")

    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

        filtered = [p for p in products if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=filtered)

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
