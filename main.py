import os
from flask import Flask, render_template,session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something secret'
app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


#initializing the imported modules
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

#defines the roles table using SQLAlchemy ORM
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	
	#defining relationship with users table
	users= db.relationship('User', backref='role')

	def __repr__(self):
		return '<Role %r>' % self.name

#defines the users table using SQLAlchemy ORM
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)

	#defining relationship iwth the roles table
	rold_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username


class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))



@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name

@app.route('/user/magic')
def google():
	return redirect('http://www.google.com')


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




