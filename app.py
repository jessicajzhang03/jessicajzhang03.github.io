from flask import Flask, render_template, request, url_for 
import jinja2 
from flask_frozen import Freezer 

app = Flask(__name__) 
freezer = Freezer(app) 

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	"""Launches page"""
	return render_template('index.html') 

@app.route('/math')
@app.route('/math.html')
def math(): 
    return render_template('math.html')

poems_list = [
    {'title':'Le Lac','author':'Lamartine','keyword':'le-lac'},
    {'title':'First Fig','author':'Edna St. Vincent Millay','keyword':'first-fig'}
]

@app.route('/poems')
@app.route('/poems.html')
@app.route('/poems/') 
def poems(): 
    return render_template('poems.html',title='Poems',poems=poems_list)

@app.route('/poems/<keyword>') 
@app.route('/poems/<keyword>.html')
def poem(keyword): 
    url = 'poems/' + keyword + '.html'
    return render_template(url,title=keyword)

@app.route('/fun') 
@app.route('/fun.html')
def fun(): 
    return render_template('fun.html') 

if __name__ == '__main__': 
    freezer.freeze() 
    freezer.run(debug=True)
