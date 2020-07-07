from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("shop.html")

@app.route("/shop.html")
def shop():
    return render_template("shop.html")
    
@app.route("/hari")
def salvador():
    return "Hello, Hari"

@app.route("/shop_2.html")
def shop_2():
    return render_template("shop_2.html")

@app.route("/shop_3.html")
def shop_3():
    return render_template("shop_3.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/cart.html")
def cart():
    return render_template("cart.html")


@app.route("/contact.html")
def checkout():
    return render_template("checkout.html")


@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
  #We made two new changes