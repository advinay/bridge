from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from .utils import load_equipe,load_rencontres,tirage_global


# Create database connection object
db = SQLAlchemy(app)


# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
@app.route('/index/')
def index():


  tirage_global(db)
  results=load_equipe()


  rencontres=load_rencontres()

  return render_template('index.html',table=results,matches=rencontres)


@app.route('/unesimu')
def unesimu():


  tirage_global(db)
  results=load_equipe()


  rencontres=load_rencontres()

  return render_template('unesimu.html',table=results,matches=rencontres)




if __name__ == "__main__":
    app.run()




