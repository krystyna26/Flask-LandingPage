from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html') 

@app.route('/ninjas')
def projects():
	return render_template('ninjas.html') 

@app.route('/dojos/new')
def create_user():
    return render_template('dojos.html') 

app.run(debug=True)