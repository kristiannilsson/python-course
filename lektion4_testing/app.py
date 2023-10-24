from flask import Flask, request
import json

app = Flask(__name__)


def get_fruits():
    with open("fruits.json") as f:
        return json.load(f)


@app.route("/fruits", methods=["GET"])
def get_all_fruits():
    fruits = get_fruits()
    return {"drinks": fruits}


@app.route("/fruits", methods=["POST"])
def add_new_fruit():
    fruits = get_fruits()
    fruits.append({"name": request.json.get("name"), "color": request.json.get("color")})
    with open("fruits.json", "w") as f:
        json.dump(fruits, f)
    return {"msg": "Fruit added successfully!"}


@app.route("/fruits", methods=["DELETE"])
def delete_fruit():
    fruit_to_remove = request.json.get("name")
    fruits = get_fruits()
    fruits = list(filter(lambda fruit: fruit["name"] != fruit_to_remove, fruits))
    return {"msg": "Fruit deleted sucessfully!"}

if __name__ == "__main__":
    app.run(debug=True)
