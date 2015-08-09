import re
import os
from flask import Flask, render_template,session, redirect, url_for, flash, request
from flask.ext.runner import Runner
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import requests



app = Flask(__name__)
app.config['SECRET_KEY'] = 'something secret'


#initializing the imported modules
runner = Runner(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class LogInForm(Form):
	email = StringField('email', validators=[Required()])
	password = StringField('password', validators=[Required()])
	submit = SubmitField('Login')


class SignUpForm(Form):
	email = StringField('email', validators=[Required()])
	password = StringField('password', validators=[Required()])
	submit = SubmitField('SIGNUP')


@app.route('/', methods=['GET', 'POST'])
def index():
	form = LogInForm()
	if form.validate_on_submit():
		

		session['email'] = form.email.data
		session['password'] = form.password.data
	

		data = {'email':session['email'], 'password':session['password']}
	
		if requests.get('http://hosting.otterlabs.org/huynhbrian/piazzahack/Login.php', data).text == '{"loginApproved":true}':
			json = requests.get("http://hosting.otterlabs.org/huynhbrian/piazzahack/Home.php", {"username":session["email"]}).json()
						
			return render_template('profile.html', name=session['email'], json=json)		
		else:
			return redirect(url_for('index'))
	
	return render_template('index.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUpForm()
	if form.validate_on_submit():
		session['email'] = form.email.data
		session['password'] = form.password.data


		data = {'email':session['email'], 'password':session['password']}

		requests.post('http://hosting.otterlabs.org/huynhbrian/piazzahack/Signup.php', data)

		json = requests.get("http://hosting.otterlabs.org/huynhbrian/piazzahack/Home.php", {'username':session['email']}).json()

		return render_template('profile.html', name=session['email'], json=json)

	return render_template('signup.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
	#get the username from the session's redirect args
	json = requests.get("http://hosting.otterlabs.org/huynhbrian/piazzahack/Home.php", {"username":session["email"]}).json()
	
	#return render_template('profile.html', username=username, error_id_list=error_id_list, error_type_list=error_type_list, etc...)
	return render_template('profile.html', name="Peter", json=json)




#nicer error handling
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500



if __name__ == '__main__':
	runner.run()




