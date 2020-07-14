from flask import Flask, render_template, request 
import jinja2 

app = Flask(__name__) 

@app.route('/',methods=['GET'])
def start_page():
	"""Launches page"""
	return render_template('index.html') 

@app.route('/cindy',methods=['GET','POST'])
@app.route('/secret',methods=['GET','POST'])
def cindy_page(): 
    return render_template('cindy.html')

@app.route('/math',methods=['GET','POST'])
def math_page(): 
    return render_template('math.html')

@app.route('/latex-asy',methods=['GET','POST'])
def latex_page(): 
    return render_template('latex-asy.html')
