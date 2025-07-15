from flask import Flask, render_template
import json
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))

@app.route('/items')
def show_items():
    # Read items from JSON file
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []
    
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
