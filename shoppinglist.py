import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
items = []

@app.route("/")
def get_index():
    total = 0
    for i in items:
        total += i['total']
        total = round(total,2)
    return render_template("index.html", items = items, total=total)
    
@app.route("/add_item", methods=["POST","GET"])
def add_item():
    quantity = request.form["quantity"]
    quantity_float = float(quantity)
    price = float(request.form["price"])
    item = {
        'item':request.form["shopping_item"],
        'quantity':quantity,
        'price':price,
        'total': round(quantity_float * price, 2)
    }
    items.append(item)
    return redirect("/")
    
@app.route("/<item>/remove", methods=["POST","GET"])
def remove_item(item):
    for i in items:
        if i['item'] == item:
            items.remove(i)
    return redirect("/")
    
@app.route("/<item>/change", methods=["POST", "GET"])
def change(item):
    item = item
    for i in items:
        if i['item'] == item:
            item = i
    return render_template("change.html", item=item)
    
@app.route("/<item>/change/new", methods=["POST", "GET"])
def change_quantity(item):
    print(item)
    new_quantity = request.form["new_quantity"]
    new_quantity_float = float(new_quantity)
    new_price = float(request.form["new_price"])
    for i in items:
        if i['item'] == item:
            i['quantity'] = new_quantity
            i['price'] = new_price
            i['total'] = round(new_quantity_float * i['price'], 2)
            print(i)
    return redirect("/")


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))