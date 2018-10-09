# import necessary libraries
from flask import Flask, render_template, request, jsonify, Blueprint
import ast


# create instance of Flask app
app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

# create route that renders index.html template
@app.route("/")
def index():

  return render_template("index.html")

# create route that sends text to Wit.AI
@app.route("/api/text", methods=["POST"])
def sendTextToWit():

	data = request.data.decode("utf-8") 
	text_dict = ast.literal_eval(data)
	print("Received text in server: ", text_dict["text"])
	text = text_dict["text"]

	return jsonify(text)


   # return render_template("form.html")



if __name__ == "__main__":
    app.run(debug=True)