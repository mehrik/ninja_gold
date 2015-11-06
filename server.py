from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'MaricIsANinja'

consolelog = []

@app.route('/')
def index():
	try:
		session['gold']
		session['log']
	except:
		session['gold'] = 0
		session['log'] = ()
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	if request.form['action'] == 'farm':
		goldearned = random.randrange(10,21)
		session['gold'] += goldearned
		consolelog.insert(0, 'Earned' + ' ' +str(goldearned)+ ' ' + 'golds from the farm!')
	elif request.form['action'] == 'cave':
		goldearned = random.randrange(5,11)
		session['gold'] += goldearned
	elif request.form['action'] == 'house':
		goldearned = random.randrange(2,6)
		session['gold'] += goldearned
	else:
		gamble = round(random.random())
		if gamble == 0:
			session['gold'] += random.randrange(0,51)
		else:
			session['gold'] -= random.randrange(0,51)
			if session['gold'] < 0:
				session['gold'] = 0
	session['log'] = consolelog
	print session['log']
 	return redirect('/')

app.run(debug=True)