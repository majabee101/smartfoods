from flask import Flask, render_template, request, jsonify


app = Flask(__name__, static_folder="./templates", static_url_path="/templates")
app.debug=True

username = "Samj"
currentBudget = 350


@app.route("/")
def mainPage():

    print("User connected to the mainpage")


    return render_template("mainpage.html", user= username, budget=currentBudget)

@app.route("/homepage", methods=["GET", "POST"])
def homePage():

    print("User connected to the homepage")

    return render_template("homepage.html",user= username, budget=currentBudget)


@app.route("/foodpage", methods=["GET", "POST"])
def foodPage():

    print("User connected to the foodpage")

    return render_template("foodpage.html")

@app.route("/analytics", methods=["GET", "POST"])
def Analytics():

    print("User connected to the foodpage")

    return render_template("analytics.html")

@app.route("/map", methods=["GET", "POST"])
def Map():

    print("User connected to the map")

    return render_template("map.html")


@app.route("/recipes", methods=["GET", "POST"])
def Recipes():

    print("User connected to the recipe page")

    return render_template("recipes.html")


@app.route("/vouchers", methods=["GET", "POST"])
def Vouchers():

    print("User connected to the voucher page")

    return render_template("vouchers.html")

@app.route("/budget", methods=["GET", "POST"])
def changeBudget():
    if request.method == "POST":
        global currentBudget
        newBudget = request.form.get("new_budget")
        print(newBudget)
        currentBudget = newBudget
        return jsonify({"new_budget":newBudget})

    return render_template("budget.html", user= username, budget=currentBudget)




if __name__ == "__main__":
    app.run()