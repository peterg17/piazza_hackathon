import os
from flask import Flask, render_template,session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something secret'


#initializing the imported modules
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class LogInForm(Form):
	email = StringField('email', validators=[Required()])
	password = StringField('password', validators=[Required()])
	submit = SubmitField('Login')



@app.route('/', methods=['GET', 'POST'])
def index():
	form = LogInForm()
	if form.validate_on_submit():
		#old_name = session.get('name')
		#if old_name is not None and old_name != form.name.data:
		#	flash('Looks like you have changed your name!')
		
		#get data from wtforms
		session['email'] = form.email.data
		session['password'] = form.password.data
		flash('submitted your info!')
	
		form.name.data = ''

		return redirect(url_for('index'))
	
	return render_template('index.html', form=form, name=session.get('name'))



@app.route('/profile')
def profile():
	#put in profile-specific stuff and nice graphs
	

	#return render_template('profile.html', username=username, error_id_list=error_id_list, error_type_list=error_type_list, etc...)
	pass

#nicer error handling
#REMEMBER TO ADD 404.html
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#REMEMBER TO ADD 500.html
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500



if __name__ == '__main__':
	manager.run()




