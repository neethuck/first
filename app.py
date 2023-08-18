from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


services = [
    {"name": "Catering", "description": "We provide delicious catering services for your special events.", "image": "Catering.jpg"},
    {"name": "Private Events", "description": "Host your private events with us and enjoy a memorable experience.", "image": "Private Events.jpg"},
    {"name": "Delivery", "description": "Get your favorite dishes delivered to your doorstep with our fast delivery service.", "image": "Delivery.jpg"}
]

dishes = [
    {"name": "Pizza", "description": "Delicious pizza with various toppings.", "image": "pizza.jpg"},
    {"name": "Burger", "description": "Juicy burger with fries.", "image": "burger.jpg"},
    {"name": "Pasta", "description": "Homemade pasta with a choice of sauces.", "image": "pastha.jpg"},
    {"name": "Sandwich", "description": "Fresh and healthy sandwich with a mix of greens.", "image": "sandwich.jpg"}
]

booked_tables = set()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        table_number = request.form.get('table_number')
        
        if not table_number.isdigit():
            flash('Table number must be a valid number', 'error')
        else:
            table_number = int(table_number)
            if table_number > 100:
                flash('Table number cannot be greater than 100', 'error')
            elif table_number in booked_tables:
                flash('Table already booked', 'error')
            else:
                booked_tables.add(table_number)
                flash('Table booked successfully', 'success')
        
        return redirect(url_for('index'))

    return render_template('index.html', services=services, dishes=dishes, booked_tables=booked_tables)

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
