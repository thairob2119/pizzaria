from flask import Flask, render_template, request
from menuitems import menu as menu_items

cart=[] # hold all of cart items

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/menu')
def menu():
    return render_template("menu.html", items=menu_items)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == "GET":
        return render_template("orderform.html", items=menu_items)
    else:
        index = int(request.form.get('item'))
        quantity = int(request.form.get('quantity'))
        instructions = request.form.get('instructions')
        ordered_item = menu_items[index]
        cost = ordered_item.get('price')

        cart_item = {
            'order_number': len(cart) + 1,
            'item_index': index,
            'instructions': instructions,
            'cost': cost,

        }

        cart.append(cart_item)

        return render_template('confirm.html', pizza_name=ordered_item.get('item'), price_of_item=ordered_item.get('price'), quantity=quantity, cost=f'{cost:.2f}', instructions = instructions)

@app.route('/cart')
def show_cart():
    if len(cart) == 0:
        return render_template('orderform.html', items=menu_items) # move user to order.form when no items in cart
    else:
        # loop trou thecrt list and show teh item nameestee, quanna, anna cosstee for teh itelm il ec les
        # alse calcu u torta cosstee of teh crt anna printe lat ta scren rond toh tu desibles
        return cart

