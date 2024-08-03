#importing libraries
import os
from flask.helpers import url_for
import numpy as np
import flask
import pickle
from werkzeug.utils import secure_filename
#importing the prediction funtion from gnn code
from gnncode import pred


#creating instance of the class
app = Flask(__name__, template_folder='templates')

#to tell flask what url shoud trigger the function index()
@app.route('/')
def index():
<<<<<<< HEAD
    if request.method == 'POST':
		file = request.files.get('file')
		img_bytes = file.read()
		prediction_name = pred(img_bytes)
        return redirect(url_for('result',name=prediction_name))
=======
>>>>>>> 5a1976f97ddff911eee230a9cb0282182ec36dfb
    return render_template('index.html')

#@app.route('/result/')
@app.route('/result/', methods=['GET', 'POST'])
<<<<<<< HEAD
def result(name):
		return render_template('result.html',name)
=======
def upload_file():
	if request.method == 'POST':
		file = request.files.get('file')
		img_bytes = file.read()
		prediction_name = pred(img_bytes)
		return render_template('result.html', name=prediction_name.lower())
>>>>>>> 5a1976f97ddff911eee230a9cb0282182ec36dfb
                         
@app.route('/faq/')
def faq():
    return render_template('faq.html')
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/ftldni/')
def ftldni():
    return render_template('https://cind.ucsf.edu/research/grants/frontotemporal-lobar-degeneration-neuroimaging-initiative-0')

if __name__ == "__main__":
    app.run(debug=True)
