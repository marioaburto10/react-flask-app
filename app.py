# import necessary libraries
from flask import Flask, render_template, request, jsonify, Blueprint
import ast
import requests
import json
from wit import Wit
from config import wit_access_token
from handleWitResponse import handle_response


# create instance of Flask app
app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

# create route that renders index.html template
@app.route("/")
def index():

  return render_template("index.html")

# create a post route that gets data from React and axios
@app.route("/api/text", methods=["POST"])
def consult_with_wit():

	# receiving data from axios and getting the text value from it
	data = request.get_json()
	text = data["text"]
	print(text)

	# sending the text to wit.ai and receiving a response
	client = Wit(access_token=wit_access_token)
	resp_content = client.message(text)

	print("RESPONSE CONTENT FROM WIT.AI: ", resp_content)

	# based on the response from wit,
	# we will perform an action (hit an API perhaps) and return back results as a string
	final_output = handle_response(resp_content)

	# send the results to axios to send to React so that the broswer can speak the results
	return jsonify(final_output)


if __name__ == "__main__":
    app.run(debug=True)