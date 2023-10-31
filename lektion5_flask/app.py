from flask import Flask, request, render_template, url_for

app = Flask(__name__)

#flera decorators per route
@app.route("/")
@app.route("/home", methods=["POST"]) #utan methods är GET default
@app.route("/index")
def hello_world():
    return render_template("index.html", form_url=url_for("login"))


#dynamisk route så att man kommer åt det sista i URL:en som ett argument
@app.route("/recipes/<recipe_id>")
def recipe_one(recipe_id):
    return {"id": recipe_id}

@app.route("/login", methods=["POST"])
def login():
    print(request.json) #kommer åt all data som skickas i body
    return "works"

"""
1. venv
2. installera flask
3. hello world
4. flera routes
5. <id> i route, typing
6. request objektet
"""