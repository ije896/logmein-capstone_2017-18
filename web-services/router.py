from flask import Flask, request
from pages import Index, Results
app = Flask(__name__)

# Index page
@app.route('/')
def index():
	return Index.Index.page()

# Results page
@app.route('/results', methods = ['POST', 'GET'])
def results():
	return Results.Results.page(request)


# MAIN

app.run(debug = True, threaded = True)

