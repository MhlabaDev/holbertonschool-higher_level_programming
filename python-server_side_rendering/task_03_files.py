from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))

def read_json_products():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_products():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, ValueError):
        return []

@app.route('/products')
def show_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products = filtered_products
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
