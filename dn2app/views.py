from flask import Flask,render_template,url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from .utils import load_equipe,load_rencontres,tirage_global,stats


# Create database connection object
db = SQLAlchemy(app)


# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
@app.route('/index/')
def index():


  return render_template('index.html')


@app.route('/unesimu/')
def unesimu():


  (results,rencontres)=tirage_global(db)


  return render_template('unesimu.html',table=results,matches=rencontres)


@app.route('/stat')
def stats_fin():

	stats(db)

	return render_template('stats.html')




if __name__ == "__main__":
    app.run()




