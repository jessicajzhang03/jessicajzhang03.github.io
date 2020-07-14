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

poems_list = [
    {'title':'Le Lac', 'author': 'Lamartine','text':['yay'],'keyword':'le_lac'},
    {'title':'First Fig','author':'Edna St. Vincent Millay',
    'text':['My candle burns at both ends','<span class="indent">It will not last the night</span>','But ah, my foes, and oh, my friends—','<span class="indent">It gives a lovely light!</span>'],'keyword':'first_fig'}
]
poem_kw = {'le_lac':0,'first_fig':1}

@app.route('/poems')
def poems(): 
    return render_template('poems.html',poems=poems_list)

@app.route('/poems/<keyword>') 
def poem(keyword): 
    poem = poems_list[poem_kw[keyword]]
    return render_template('poem.html',poem=poem)
