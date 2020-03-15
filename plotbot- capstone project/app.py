from textgenrnn import textgenrnn
from flask import Flask, redirect, url_for, request
import tensorflow as tf
from flask_cors import CORS
app = Flask(__name__)

temp = 0.5
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/generate_sentences/<genre>/<prefix>/<n_sentences>',methods = ['GET'])
def generate_sentences(genre, prefix, n_sentences):
	s = generate1(genre,prefix,n_sentences)
	return s

def generate1(genre,prefix,n_sentences):
	print(genre + " " + prefix + " " + n_sentences)
	n_sentences = int(n_sentences)
	with tf.Session() as sess:
		td = textgenrnn('weights/' + genre + '.hdf5')
		text = td.generate(return_as_list=True, prefix=prefix, temperature=temp, n_sentences=n_sentences)[0]
	print(type(text))
	print(text)
	text = text.replace("<s>"," ")
	return text

@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('generate_sentences',genre = 'crime', prefix = user, n_sentences = "2"))

if __name__ == '__main__':
   app.run(debug=True)