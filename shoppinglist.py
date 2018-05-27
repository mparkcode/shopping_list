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
    print(items)
    return redirect("/")
    
@app.route("/<item>/remove", methods=["POST","GET"])
def remove_item(item):
    for i in items:
        if i['item'] == item:
            items.remove(i)
    return redirect("/")

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))