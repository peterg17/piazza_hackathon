#import modules here
from flask import Flask
from flask.ext.script import Manager


app = Flask(__app__)

#initialize objects here
manager = Manager(app)



#define home page
app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')




if __name__ == '__main__':

