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
	goldearned = 0;

	#Determines how much gold is earned or lost
	if request.form['action'] == 'farm':
		goldearned = random.randrange(10,21)
	elif request.form['action'] == 'cave':
		goldearned = random.randrange(5,11)
	elif request.form['action'] == 'house':
		goldearned = random.randrange(2,6)
	elif request.form['action'] == 'casino':
		gamble = round(random.random())
		goldearned = random.randrange(-50,51)
		if goldearned > 0:
			consolelog.insert(0, 'Entered a casino and won' + ' ' +str(goldearned)+ ' ' + 'golds... YAY! ' + date)
		else:
			consolelog.insert(0, 'Entered a casino and lost' + ' ' +str(goldearned * -1)+ ' ' + 'golds... ouch.. ' + date)
	session['gold'] += goldearned

	#If gold goes below, zero, it will stay at 0
	if session['gold'] < 0:
		session['gold'] = 0

	#Print this line if the gold earned was not from casino
	if goldearned > 0 and request.form['action'] != 'casino':
		consolelog.insert(0, 'Earned' + ' ' +str(goldearned)+ ' ' + 'golds from the ' + request.form['action'] +'! ' + date)
	session['log'] = consolelog

	#Allows user to reset their activities log and gold amount
	if request.form['action'] == 'reset':
		session['gold'] = 0
		del session['log'][:]

	print session['log']
 	return redirect('/')

app.run(debug=True)