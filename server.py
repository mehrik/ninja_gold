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
		session['log'] = []
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	date = datetime.now().strftime('(%Y/%m/%d %r)')
	if request.form['action'] == 'reset':
		session.pop('gold')
		session.pop('log')
	elif request.form['action'] == 'farm':
		goldearned = random.randrange(10,21)
		session['gold'] += goldearned
		consolelog.insert(0, 'Earned' + ' ' +str(goldearned)+ ' ' + 'golds from the farm! ' + date)
	elif request.form['action'] == 'cave':
		goldearned = random.randrange(5,11)
		session['gold'] += goldearned
		consolelog.insert(0, 'Earned' + ' ' +str(goldearned)+ ' ' + 'golds from the cave! ' + date)
	elif request.form['action'] == 'house':
		goldearned = random.randrange(2,6)
		session['gold'] += goldearned
		consolelog.insert(0, 'Earned' + ' ' +str(goldearned)+ ' ' + 'golds from the house! ' + date)
	else:
		gamble = round(random.random())
		if gamble == 0:
			goldearned = random.randrange(0,51)
			session['gold'] += goldearned
			consolelog.insert(0, 'Entered a casino and won' + ' ' +str(goldearned)+ ' ' + 'golds... YAY! ' + date)
		else:
			goldearned = random.randrange(0,51)
			session['gold'] -= goldearned
			consolelog.insert(0, 'Entered a casino and lost' + ' ' +str(goldearned)+ ' ' + 'golds... ouch.. ' + date)
			if session['gold'] < 0:
				session['gold'] = 0
	session['log'] = consolelog
	print session['log']
 	return redirect('/')

app.run(debug=True)