# import necessary libraries
from flask import Flask, render_template, request, jsonify, Blueprint
import ast
import requests
import json


# create instance of Flask app
app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

# create route that renders index.html template
@app.route("/")
def index():

  return render_template("index.html")

# create route that sends text to Wit.AI
@app.route("/api/text", methods=["POST"])
def sendTextToWit():

	wit_access_token = 'IQBNTQDDXPTPGJRWXLSDYUQBXXW4A5S3'
	API_ENDPOINT = "https://api.wit.ai/message"

	data = request.data.decode("utf-8") 
	data_dict = ast.literal_eval(data)
	text = data_dict["text"]

	question = {'q': text}

	# print("Received text in server: ", text)

	# defining headers for HTTP request
	headers = {'Authorization': 'Bearer ' + wit_access_token}

	# making an HTTP post request
	resp = requests.get(API_ENDPOINT, headers=headers, params=question)

	# converting response content to JSON format
	respContent = json.loads(resp.content)

	print("CONTENT FROM WIT.AI: ", respContent)




	return jsonify(respContent)


  # return render_template("form.html")



if __name__ == "__main__":
    app.run(debug=True)