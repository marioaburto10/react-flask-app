# import necessary libraries
from flask import Flask, render_template, request, jsonify, Blueprint

# create instance of Flask app
app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)